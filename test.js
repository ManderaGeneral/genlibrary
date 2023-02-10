/**
 * @jest-environment jsdom
 */

// https://jestjs.io/docs/configuration#testenvironment-string

const Vec2 = require("./vec2");

test("Vec2 initializing", () => {
    expect(new Vec2().x).toBe(0);
})
