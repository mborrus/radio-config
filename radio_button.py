#!/usr/bin/env python3
import lgpio
import os
import time

CHIP = 0
PIN = 23
SAMPLES = 10       # number of samples to check
SAMPLE_DELAY = 0.05 # 50ms between samples
COOLDOWN = 2       # seconds between allowed changes

h = lgpio.gpiochip_open(CHIP)
lgpio.gpio_claim_input(h, PIN, lgpio.SET_PULL_UP)

last_change = 0

def is_really_pressed():
    """Check if button is consistently pressed across multiple samples"""
    pressed_count = 0
    for _ in range(SAMPLES):
        if lgpio.gpio_read(h, PIN) == 0:  # 0 = pressed (pulled low)
            pressed_count += 1
        time.sleep(SAMPLE_DELAY)
    return pressed_count >= SAMPLES - 1  # allow 1 glitch

print("Button monitor started (polling mode)")
was_pressed = False

while True:
    pressed = lgpio.gpio_read(h, PIN) == 0
    
    if pressed and not was_pressed:
        # Button just went down - verify it is real
        if is_really_pressed():
            now = time.time()
            if now - last_change >= COOLDOWN:
                last_change = now
                print("Next Station...")
                os.system("mpc next")
        was_pressed = True
    elif not pressed:
        was_pressed = False
    
    time.sleep(0.1)
