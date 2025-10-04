#!/bin/bash

# Script to add bottom navigation to all email templates

# Find all HTML files in the emails directory
find emails -name "*.html" -type f | while read -r file; do
    echo "Processing: $file"
    
    # Extract the filename without extension for the download name
    filename=$(basename "$file" .html)
    
    # Add bottom navigation CSS before the closing </style> tag
    sed -i '' '/^  <\/style>$/i\
    \
    /* Bottom Navigation */\
    .bottom-nav {\
      position: fixed;\
      bottom: 0;\
      left: 0;\
      right: 0;\
      background: #FFFFFF;\
      border-top: 1px solid #e2e8f0;\
      padding: 12px 16px;\
      z-index: 1000;\
      display: flex;\
      justify-content: center;\
      box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.1);\
    }\
\
    .download-btn {\
      background: #0d9488;\
      color: #FFFFFF;\
      border: none;\
      border-radius: 8px;\
      padding: 12px 24px;\
      font-size: 14px;\
      font-weight: 500;\
      font-family: '\''Epilogue'\'', -apple-system, BlinkMacSystemFont, '\''Segoe UI'\'', Roboto, Arial, sans-serif;\
      cursor: pointer;\
      display: flex;\
      align-items: center;\
      gap: 8px;\
      transition: background-color 0.2s ease;\
    }\
\
    .download-btn:hover {\
      background: #0b7a6b;\
    }\
\
    .download-btn .material-icons {\
      font-size: 18px;\
    }\
\
    /* Dark mode styles for bottom nav */\
    .force-dark .bottom-nav {\
      background: #0a1216;\
      border-top-color: #1e293b;\
    }\
\
    .force-dark .download-btn {\
      background: #2dd4bf;\
      color: #0a1216;\
    }\
\
    .force-dark .download-btn:hover {\
      background: #26c4b1;\
    }\
\
    @media (prefers-color-scheme: dark) {\
      .bottom-nav {\
        background: #0a1216;\
        border-top-color: #1e293b;\
      }\
\
      .download-btn {\
        background: #2dd4bf;\
        color: #0a1216;\
      }\
\
      .download-btn:hover {\
        background: #26c4b1;\
      }\
    }' "$file"
    
    # Add bottom padding to body
    sed -i '' 's/body, table, td, a { font-family: '\''Epilogue'\'', -apple-system, BlinkMacSystemFont, '\''Segoe UI'\'', Roboto, Arial, sans-serif !important; color: #05151d !important; }/body, table, td, a { font-family: '\''Epilogue'\'', -apple-system, BlinkMacSystemFont, '\''Segoe UI'\'', Roboto, Arial, sans-serif !important; color: #05151d !important; padding-bottom: 80px; }/' "$file"
    
    # Add bottom navigation HTML and script before closing </body> tag
    sed -i '' '/^<\/body>$/i\
\
  <!-- Bottom Navigation -->\
  <div class="bottom-nav">\
    <button class="download-btn" onclick="downloadHTML()">\
      <span class="material-icons">download</span>\
      Download HTML\
    </button>\
  </div>\
\
  <script>\
    function downloadHTML() {\
      // Get the current page'\''s HTML content\
      const htmlContent = document.documentElement.outerHTML;\
      \
      // Create a blob with the HTML content\
      const blob = new Blob([htmlContent], { type: '\''text/html'\'' });\
      \
      // Create a temporary URL for the blob\
      const url = URL.createObjectURL(blob);\
      \
      // Create a temporary link element and trigger download\
      const link = document.createElement('\''a'\'');\
      link.href = url;\
      link.download = '\''"$filename".html'\'';\
      document.body.appendChild(link);\
      link.click();\
      document.body.removeChild(link);\
      \
      // Clean up the URL\
      URL.revokeObjectURL(url);\
    }\
  </script>' "$file"
    
    echo "Added bottom navigation to: $file"
done

echo "Bottom navigation added to all email templates!"
