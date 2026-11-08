// Browser test for the cyberdeck mission screen.
// Needs Node and Playwright (npm i -D playwright && npx playwright install chromium).
// Run from the repo root:  node tests/mission_screen_test.js [screenshot-folder]
const path = require("path");
const assert = require("assert");
const { chromium } = require("playwright");

const PAGE = "file://" + path.resolve(__dirname, "..", "mission-02-cyberdeck", "mission-screen", "index.html");
const SHOTS = process.argv[2];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
  await page.goto(PAGE);

  // 1. Starts NO-GO with an empty checklist.
  assert.strictEqual(await page.textContent("#goBanner"), "NO-GO");

  // 2. Parsing console lines from the robot programs.
  const parsed = await page.evaluate(() => window.MissionControl.parseConsole([
    "PREFLIGHT battery=87",
    "PREFLIGHT motor=LF port=1 ok=1 temp=32",
    "PREFLIGHT motor=RB port=10 ok=0 temp=na",
    "PREFLIGHT result=NO-GO",
    "TLM t=4.2 bat=86 event=site detail=Jezero_Delta",
    "some other console noise",
  ].join("\n")));
  assert.strictEqual(parsed.battery, 86);
  assert.strictEqual(parsed.preflight, "NO-GO");
  assert.deepStrictEqual(parsed.motors[1], { id: "RB", port: "10", ok: false, temp: null });
  assert.deepStrictEqual(parsed.events[0], { t: 4.2, event: "site", detail: "Jezero Delta" });

  // 3. Checking every item gives GO, a NO-GO rover check overrides it, a GO check restores it.
  const boxes = await page.$$("#checklist input");
  for (const b of boxes) await b.check();
  assert.strictEqual(await page.textContent("#goBanner"), "GO FOR LAUNCH");
  await page.fill("#consoleInput", "PREFLIGHT battery=40\nPREFLIGHT result=NO-GO");
  await page.click("#readBtn");
  assert.strictEqual(await page.textContent("#goBanner"), "NO-GO: ROVER CHECK");
  assert.strictEqual(await page.textContent("#battery"), "40%");
  await page.fill("#consoleInput", "PREFLIGHT battery=92\nPREFLIGHT motor=LF port=1 ok=1 temp=31\nPREFLIGHT result=GO");
  await page.click("#readBtn");
  assert.strictEqual(await page.textContent("#goBanner"), "GO FOR LAUNCH");
  assert.match(await page.textContent("#motors"), /LF1/);

  // 4. Countdown: 5 s, hold, resume with the Space key, then T+ after liftoff.
  await page.selectOption("#countLength", "5");
  assert.strictEqual(await page.textContent("#clock"), "T-00:05");
  await page.click("#startBtn");
  await page.waitForTimeout(1300);
  await page.click("#startBtn");                       // hold
  const held = await page.textContent("#clock");
  assert.match(held, /^T-00:0[34]$/);
  assert.strictEqual(await page.textContent("#clockState"), "HOLDING");
  await page.waitForTimeout(1000);
  assert.strictEqual(await page.textContent("#clock"), held); // frozen while holding
  await page.click("body");
  await page.keyboard.press("Space");                  // resume
  await page.waitForTimeout(4600);
  assert.match(await page.textContent("#clock"), /^T\+00:0\d$/);
  assert.strictEqual(await page.textContent("#clockState"), "MISSION IN PROGRESS");
  assert.match(await page.textContent("#log"), /LIFTOFF/);

  // 5. Typing in the mission name must not trigger the shortcuts.
  await page.click("#missionName");
  await page.keyboard.press("r");
  assert.strictEqual(await page.textContent("#clockState"), "MISSION IN PROGRESS");

  // 6. Reset key.
  await page.click("body");
  await page.keyboard.press("r");
  assert.strictEqual(await page.textContent("#clock"), "T-00:05");

  if (SHOTS) await page.screenshot({ path: path.join(SHOTS, "mission-screen-1280.png") });

  // 7. Fits a small screen without sideways scrolling.
  const phone = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await phone.goto(PAGE);
  const overflow = await phone.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  assert.strictEqual(overflow, false, "page scrolls sideways at 390px");
  if (SHOTS) await phone.screenshot({ path: path.join(SHOTS, "mission-screen-390.png"), fullPage: true });

  assert.deepStrictEqual(errors, []);
  await browser.close();
  console.log("mission screen: all checks passed");
})().catch((e) => { console.error(e); process.exit(1); });
