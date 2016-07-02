#!/usr/bin/python3
import hexchat

__module_name__ = "ascii-art"
__module_version__ = "0.1.0"
__module_description__ = "bunch of quick ascii art"

SHRUG = "¯\_(ツ)_/¯"
FLIP = "(╯°□°)╯︵ ┻━┻"
UNFLIP = "┬─┬﻿ ノ( ゜-゜ノ)"


def shrug(word, word_eol, userdata):
    """/shrug <text> - appends '¯\_(ツ)_/¯' to the end of the message"""

    if len(word_eol) > 1:
        send(word_eol[1] + ' ' + SHRUG)
    else:
        send(SHRUG)


def flip(word, word_eol, userdata):
    """/flip <text> - prepends '(╯°□°)╯︵ ┻━┻' to the end of the message"""

    if len(word_eol) > 1:
        send(word_eol[1] + ' ' + FLIP)
    else:
        send(FLIP)


def unflip(word, word_eol, userdata):
    """/unfip <text> - appends '┬─┬﻿ ノ( ゜-゜ノ)' to the end of the message"""

    if len(word_eol) > 1:
        send(word_eol[1] + ' ' + UNFLIP)
    else:
        send(UNFLIP)


def send(message):
    channel = hexchat.get_info('channel')
    hexchat.command('MSG {0} {1}'.format(channel, message))


hexchat.hook_command("shrug", shrug, help=shrug.__doc__)
hexchat.hook_command("flip", flip, help=flip.__doc__)
hexchat.hook_command("unflip", unflip, help=unflip.__doc__)
print("Loaded " + __module_name__ + " v" + __module_version__)
