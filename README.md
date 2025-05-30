[![ActionLint](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/ActionLint.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/ActionLint.yml) 🛠️
[![Rebase](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/rebase.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/rebase.yml) 🔄
[![Bandit](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/Bandit.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/Bandit.yml) 🐍
[![Black](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/black-formatter.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/black-formatter.yml) 🎨
[![CodeQL](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/codeql.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/codeql.yml) 🔍
[![Dependabot](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/dependabot/dependabot-updates) 🤖
[![Dep Review](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/dependency-review.yml) 🧩
[![Jekyll Deploy](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/jekyll-gh-pages.yml) 🚀
[![DevSkim](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/devskim.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/devskim.yml) 🧪
[![GitLeaks](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/gitleaks.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/gitleaks.yml) 🕵️
[![Sitemap](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/sitemap.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/sitemap.yml) 🗺️
[![Greetings](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/greetings.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/greetings.yml) 👋
[![Stale](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/stale.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/stale.yml) 💤
[![MegaLinter](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/mega-linter.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/mega-linter.yml) 🦾
[![Stats](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/repo-stats.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/repo-stats.yml) 📊
[![SecDevOps](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/security-devops.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/security-devops.yml) 🛡️
[![OSSAR](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/ossar.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/ossar.yml) 🧬
[![PSSecret](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/pssecret-scanner.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/pssecret-scanner.yml) 🔑
[![Scorecard](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/scorecards.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/scorecards.yml) 🏅
[![Typos](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/typos.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/typos.yml) ✏️
[![Summary](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/summary.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/summary.yml) 📝
[![TruffleHog](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/trufflehog.yml/badge.svg)](https://github.com/Nick2bad4u/internet-archive-upload/actions/workflows/trufflehog.yml) 🐗


# Internet Archive Upload Action

- This action was originally forked from [palewire/internet-archive-upload](https://github.com/palewire/internet-archive-upload).
- It allows you to upload files or directories to the Internet Archive (archive.org) and set metadata for the uploaded items. The action supports uploading single files, multiple files, or entire directories, and it can handle various metadata fields to describe the content being uploaded.

## Inputs: _(Required)_

Input Name   | Description
------------ | ---------------------------------------------------------------------------
`access-key` | Your archive.org access key
`secret-key` | Your archive.org secret key
`identifier` | The unique identifier of the archive.org item where the file will be stored
`files`      | The file or folder path inside the action's filesystem to upload

### Supported Metadata Fields Inputs: _(Optional)_

Input Name                  | Description                                                                    | Example
--------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------
`adaptive_ocr`              | Allows deriver to skip a page that would otherwise disrupt OCR                 | true
`aspect_ratio`              | Ratio of the pixel width and height of a video stream (e.g. 4:3, 16:9)         | 4:3
`betterpdf`                 | Indicates that the derive module should create a higher quality PDF derivative | true
`bookreader-defaults`       | Bookreader display mode (e.g. mode/1up, mode/2up, mode/thumb)                  | mode/1up
`bwocr`                     | Allows deriver to OCR specific pages as B&W if color is causing failure        | 001
`call_number`               | Contributing library's local call number                                       | 6675707, NC 285.1 P9287m
`ccnum`                     | Closed Captioning Number                                                       | cc5
`closed_captioning`         | Indicates whether item contains closed captioning files (yes/no)               | yes
`color`                     | Indicates whether media is in color or black and white                         | color
`condition`                 | Condition of media (e.g. Good, Fair, Poor)                                     | Good
`condition-visual`          | Condition of artwork or printed materials                                      | Good
`contributor`               | Comma-separated list of contributors                                           | Robarts - University of Toronto
`coverage`                  | Comma-separated list of geographic or subject areas covered by item            | GB-LND
`creator`                   | Comma-separated list of creators                                               | Austen, Jane, 1775-1817, Ralph Burns
`creator-alt-script`        | Creator in alternate script                                                    | [alternate script]
`date`                      | Date of publication (YYYY, YYYY-MM, or YYYY-MM-DD)                             | 1965, 2013-05-25, [n.d.]
`description`               | Describes the media stored in the item                                         | Cinemascope homage to the city of San Francisco made by amateur filmmaker and inventor Tullio Pellegrini.
`external-identifier`       | Comma-separated list of URLs or identifiers to outside resources               | urn:publisher_catalog_id:88697 03614 2
`fixed-ppi`                 | To change the ppi to a specific resolution                                     | 300
`isbn`                      | Comma-separated list of ISBN-10 or ISBN-13                                     | 3540212507, 031294716X
`issn`                      | Comma-separated list of ISSN identifiers                                       | 2528-7788, 1943-345X
`lccn`                      | Comma-separated list of Library of Congress Call Numbers                       | 2004045278
`language`                  | Comma-separated list of languages                                              | eng, Italian, None
`licenseurl`                | URL of the copyright license                                                   | <http://creativecommons.org/licenses/by-nd/3.0/>
`notes`                     | Additional notes about the item                                                | [any string]
`oclc-id`                   | Comma-separated list of OCLC identifiers                                       | 37432884
`openlibrary`               | Deprecated. Open Library edition identifier                                    | OL2769393M
`openlibrary_author`        | Comma-separated list of Open Library authors                                   | OL52922A
`openlibrary_edition`       | Open Library edition identifier                                                | OL2769393M
`openlibrary_subject`       | Comma-separated list of Open Library subjects                                  | openlibrary_staff_picks
`openlibrary_work`          | Open Library work identifier                                                   | OL675783W
`page-progression`          | Determines direction pages will be "turned" in a book (lr/rl)                  | lr
`possible-copyright-status` | Information relevant to copyright status                                       | The Centers for Medicare & Medicaid Services Library is unaware of any copyright restrictions for this item.
`ppi`                       | Pixels per inch                                                                | 300
`publisher`                 | Publisher of the media                                                         | New York : R.R. Bowker Co.
`related-external-id`       | Comma-separated list of related external identifiers                           | urn:isbn:0671038303
`rights`                    | Rights statement                                                               | Permission is granted under the Wikimedia Foundation's ...
`scandate`                  | Date and time the media was captured                                           | 20170329201345
`scanner`                   | Machinery used to digitize or collect the media                                | scribe2.nj.archive.org
`size`                      | Size of physical item digitized                                                | 10.0
`sound`                     | Indicates whether media has sound or is silent                                 | sound
`source`                    | Source of media                                                                | folio, Comcast Cable, CD
`sponsor`                   | The person or organization that funded the digitization or collection          | Kahle-Austin Foundation
`subject`                   | Comma-separated list of subjects/topics for the item                           | France
`title`                     | The human-readable title for the item                                          | San Francisco (1955 Cinemascope film)
`title-alt-script`          | Title in alternate script                                                      | [alternate script]
`volume`                    | Volume number or name                                                          | 15
`year`                      | Year of publication (deprecated, use date)                                     | 1996

## Usage

Upload a single file with metadata:

```yaml
name: Upload a file to archive.org with metadata
jobs:

  job:
    name: Upload a file
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Upload file to archive.org
        uses: nick2bad4u/internet-archive-upload@latest
        with:
            # Required fields
            access-key: ${{ secrets.IA_ACCESS_KEY }}
            secret-key: ${{ secrets.IA_SECRET_KEY }}
            identifier: your-item
            files: your-file.jpg

            # Optional metadata fields
            title: "My Archive Title"
            creator: "Jane Doe,John Smith"
            subject: "example,archive,upload"
            date: "2025-05-29"
            language: "English"
            betterpdf: "true"
````

Upload a directory of files:

```yaml
name: Upload a directory of files to archive.org with metadata
jobs:
  job:
    name: Upload directory
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Upload directory to archive.org
        uses: nick2bad4u/internet-archive-upload@latest
        with:
          # Required fields
          access-key: ${{ secrets.IA_ACCESS_KEY }}
          secret-key: ${{ secrets.IA_SECRET_KEY }}
          identifier: your-item
          files: your-files/

          # Optional metadata fields
          title: "My Archive Title"
          creator: "Jane Doe,John Smith"
          subject: "example,archive,upload"
          date: "2025-05-29"
          language: "English"
          betterpdf: "true"
```

## Issues

If you encounter any issues or have feature requests, please open an issue in the [GitHub repository](https://github.com/nick2bad4u/internet-archive-upload/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Nick2bad4u/internet-archive-upload/blob/main/LICENSE) file for details.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## Acknowledgements

This action was originally created by [Ben Welsh](https://github.com/palewire/internet-archive-upload). It has been forked and maintained by [Nick2bad4u](https://github.com/nick2bad4u/internet-archive-upload).

<div align="center">
    <img
      src="https://github.com/Nick2bad4u/Nick2bad4u/blob/main/assets/GitHubProfileLines.gif?raw=true"
      alt="Repository Banner Line Animation"
      width="100%"
    />
</div>

# Repo Statistics

![Repo Beats](https://repobeats.axiom.co/api/embed/c1271c0a75ae77ab95116cfe318e5b9831f4182d.svg "Repobeats analytics image")

<div align="center">
    <img
      src="https://github.com/Nick2bad4u/internet-archive-upload/raw/refs/heads/main/metrics.repository.svg"
      alt="Repo Metrics"
      width="100%"
    />
</div>