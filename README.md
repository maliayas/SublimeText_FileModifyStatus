# FileModifyStatus

FileModifyStatus is a Sublime Text plugin that shows the _modified_ status of the file in the status bar. This is done through checking the undo stack.

Sublime Text itself tells if the document is dirty or not but only since the last save. This plugin however checks if the file is modified since it was ever opened.

* If the file is modified:

    ![FileModifyStatus][screenshot2]

* If the file is not modified since it was opened:

    ![FileModifyStatus][screenshot1]

## Overview

* [Installation](#installation)
* [Configuration](#configuration)
* [Donation](#donation)
* [License](#license)

## Installation

You can install the plugin via

* Package Manager by searching `FileModifyStatus`
* Git
* Downloading the [zip][] of the repo and extracting into `Packages/FileModifyStatus`

## Configuration

If the unicode icons doesn't fit your needs, you can change them via settings. They can be any string.

```js
// The marker icon/text for unmodified files
"unmodified_marker": "◯",

// The marker icon/text for modified files
"modified_marker": "◉"
```

Open you user settings file via this menu:

`Preferences > Package Settings > File Modify Status`

Your changes will require a __restart__.

## Donation

If you want to support further creative work, you can make a donation. Thanks.

<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=W2NXRPD43YSCU&amp;lc=TR&amp;item_name=Sublime%20Text&amp;item_number=FileModifyStatus&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="[paypal]" /></a>

## License

FileModifyStatus is released under the [MIT License][mit].

[mit]:         http://www.opensource.org/licenses/MIT
[screenshot1]: https://raw.github.com/maliayas/SublimeText_FileModifyStatus/master/screenshots/unmodified.png
[screenshot2]: https://raw.github.com/maliayas/SublimeText_FileModifyStatus/master/screenshots/modified.png
[zip]:         https://github.com/maliayas/SublimeText_FileModifyStatus/archive/master.zip
