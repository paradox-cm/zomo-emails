# ZOMO Health — HTML Newsletter (Mailchimp-Ready)

A zero-dependency, Mailchimp-friendly HTML email project for ZOMO Health newsletters.

## Project Structure

```
/zomo-newsletters
  /assets/images (logo.png, hero.jpg)
  index.html
  zomo-health-template-01.html
  README.md
```

## Content Source

Content in `zomo-health-template-01.html` is adapted from "Fall Newsletter.md" supplied by ZOMO Health.

## Features

- **600px table layout** optimized for email clients
- **Inline styles** for maximum compatibility
- **Hidden preheader** for better email previews
- **Hero image** support
- **Bulletproof CTA** with VML fallback for Outlook
- **Footer with unsubscribe** link using Mailchimp merge tags
- **Light/dark mode support** via `prefers-color-scheme: dark`
- **Epilogue typography** following Zomo Health design standards
- **Google Material Icons** for professional visual elements
- **Brand tokenized** values in comments for easy customization

## Mailchimp Import Instructions

### Method 1: Paste in Code
1. Copy the entire contents of `zomo-health-template-01.html`
2. In Mailchimp: Campaigns → Design Email → Code Your Own
3. Paste the code
4. Upload images to Content Studio or use absolute URLs

### Method 2: Import Zip
1. Zip the entire project folder
2. In Mailchimp: Campaigns → Design Email → Code Your Own
3. Use "Import Zip" option
4. Mailchimp will host the images from the `assets/` folder

## Customization

- Edit copy directly in the HTML file
- Keep styles inline for maximum client support
- Update placeholder links (example.com) to your live URLs
- Replace `assets/images/logo.png` and `assets/images/hero.jpg` with your actual images
- Update contact information in the "Your Zomo Health Contact" section

## Subject Line

Use this subject line in your ESP send settings:
**"Your September Partner Update: New Zomo Tools & Digital Health Strategy"**

## Zomo Health Color Palette

### Light Mode
- Background: `#FFFFFF`
- Foreground: `#0a1216`
- Primary: `#0d9488` (Teal-600)
- Muted Text: `#64748b`
- Borders: `#e2e8f0`

### Dark Mode
- Background: `#0a1216`
- Foreground: `#f8fafc`
- Primary: `#2dd4bf` (Teal-400)
- Muted Text: `#94a3b8`
- Card Background: `#0f1a21`
- Borders: `#131f27`

## Typography Standards

### Font Family
- **Primary Font:** Epilogue (Google Fonts)
- **Weights Used:** 400 (Regular), 500 (Medium), 700 (Bold)
- **Icons:** Google Material Icons for visual elements

### Type Scale Applied
- **H1 (Main Title):** 30px, font-weight: 700, line-height: 1.4
- **H2 (Section Headings):** 24px, font-weight: 700, line-height: 1.35
- **Body Large (Intro Text):** 18px, font-weight: 400, line-height: 1.7
- **Body Regular (Standard Text):** 16px, font-weight: 400, line-height: 1.6
- **Body Small (Footer):** 14px, font-weight: 400, line-height: 1.6
- **Bullet Points:** 14px, font-weight: 400, line-height: 1.7
- **Button Text:** 16px, font-weight: 500

## Validation Checklist

- [ ] Open `zomo-health-template-01.html` locally; confirm 600px layout, images, and bullets
- [ ] Test light/dark mode in Apple Mail/iOS; verify contrast on headings, muted text, and CTA
- [ ] Send tests to Gmail + Outlook; check button, list spacing, link tracking
- [ ] Verify unsubscribe merge tag `*|UNSUB|*` works in Mailchimp preview
- [ ] Zip and use "Import Zip" to confirm assets resolve

## Technical Notes

- Uses table-based layout for maximum email client compatibility
- Includes MSO (Microsoft Outlook) conditional comments
- VML button for Outlook CTA support
- No external CSS or webfonts for maximum compatibility
- Responsive design considerations included
