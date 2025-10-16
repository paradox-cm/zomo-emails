# Untitled

You are editing an HTML email repository. Update six download pages so they show only the email HTML document (doctype + head + styles + body for the email), excluding all preview UI (top toolbar, theme toggles) and excluding the bottom “Download HTML” button and any related scripts. Keep the existing download-page chrome (header with “Copy Code”, back link, container) but replace ONLY the contents of <pre id="code-content"> with an HTML-escaped version of the cleaned email HTML document.

Pairs to process (source email template -> target download page):

1. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-cbiz-template.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-cbiz-template-download.html
2. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-gallagher-template.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-gallagher-template-download.html
3. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-lockton-template.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-lockton-template-download.html
4. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-marsh-template.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-marsh-template-download.html
5. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-usi-template.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-usi-template-download.html
6. /Users/christophermena/Repos/zomo-emails/emails/newsletters/zomo-health-template-01.html
-> /Users/christophermena/Repos/zomo-emails/download-pages/zomo-health-template-01-download.html

For each source template:

- Start from the full HTML document (from <!doctype html> to </html>).
- REMOVE all preview-only UI and logic:
    - Entire elements with classes/IDs: .view-switcher, .theme-switcher, .theme-dropdown, .bottom-nav, #email-container class toggling UI, and any “Back to Email” toolbar above the email.
    - Any <script> blocks that implement preview features (e.g., switchView, toggleThemeDropdown, switchTheme) and the “downloadHTML()” function.
- KEEP email-critical elements:
    - <head> with meta tags, fonts, styles, and email CSS.
    - <body> with the email markup (preheader, email tables, content).
    - Conditional MSO styles if present.
- Preserve absolute asset URLs as-is.

Then open the corresponding target download page and REPLACE only the innerText of:
<pre id="code-content"> ... </pre>
with the HTML-escaped version of the cleaned email document (convert <, >, & to entities so it renders as code, starting with <!doctype html>).

Do NOT alter the rest of the download page structure (header/title/copy button/back link/containers, existing styles, etc.). Only change the content between the opening and closing <pre id="code-content"> tags.

Validation for each updated download page:

- The <pre id="code-content"> begins with “<!doctype html>”.
- No occurrences of these in the escaped content: “view-switcher”, “theme-switcher”, “theme-dropdown”, “bottom-nav”, “downloadHTML(”, “switchView(”, “toggleThemeDropdown(”, “switchTheme(”.
- The escaped content still includes <head> and <body> sections, fonts, styles, and the full email tables.

Finally, save all six files.