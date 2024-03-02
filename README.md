Why fix your broken Innr Zigbee lights that randomly disconnect for a few seconds when Home Assistant can fix them for you?

I have a few old bulbs that randomly disconnect from the hub for a few seconds at a time, which is mostly annoying when i try to use the switch in a room and one or two bulbs stay behind in their previous state

So i thought of a script that checks if 70% of a group of lights (group them in your configuration.yaml) is on or off and fixes the state of the remaining bulbs and let ChatGPT create it. I run that via an automation every 15 seconds, and for now it works perfectly :)


Automation:
```
alias: Fix Zigbee
description: ''
trigger:
  - platform: time_pattern
    seconds: '/30'
action:
  - service: python_script.check_and_sync_lights
    data:
      group: 'group.k1_lights'
      threshold: 70
  - service: python_script.check_and_sync_lights
    data:
      group: 'group.k2_lights'
      threshold: 70
  - service: python_script.check_and_sync_lights
    data:
      group: 'group.wz_lights'
      threshold: 70
mode: single

```
