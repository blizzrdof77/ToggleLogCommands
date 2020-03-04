# ToggleLogCommands
A [Sublime Text](https://www.sublimetext.com/) package that makes it
easy to toggle on/off command and event logging in the console view.

### Contributing
[View Source on GitHub](https://github.com/blizzrdof77/ToggleLogCommands)

### Customization Options

#### Set Custom Keyboard Shortcuts
Optionally Set custom keybindings in you `sublime-keymap` preferences file:

```
/* Toggle Log Commands (On) */
{
    "keys": ["super+k", "super+k", "super+l"],
    "command": "toggle_log_commands_on"
},
/* Toggle Log Commands (Off) */
{
    "keys": ["super+shift+k", "super+shift+k", "super+shift+l"],
    "command": "toggle_log_commands_off"
}
```