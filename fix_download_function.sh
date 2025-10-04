#!/bin/bash

# Script to fix the download function in all email templates

# Find all HTML files in the emails directory (excluding index files)
find emails -name "*.html" -type f ! -name "index.html" ! -name "templates.html" | while read -r file; do
    echo "Processing: $file"
    
    # Replace the old download function with the new one
    sed -i '' '/function downloadHTML() {/,/}/c\
    function downloadHTML() {\
      // Get the current page'\''s HTML content\
      const htmlContent = document.documentElement.outerHTML;\
      \
      // Encode the HTML content for URL\
      const encodedHtml = encodeURIComponent(htmlContent);\
      \
      // Open the code viewer page with the HTML content\
      const codeViewerUrl = `../code-pages/template.html?html=${encodedHtml}`;\
      window.open(codeViewerUrl, '\''_blank'\'');\
    }' "$file"
    
    echo "Updated download function in: $file"
done

echo "Download function updated in all email templates!"
