#!/bin/bash

# Script to clean up all email templates and ensure they have proper bottom navigation

# Find all HTML files in the emails directory (excluding index files)
find emails -name "*.html" -type f ! -name "index.html" ! -name "templates.html" | while read -r file; do
    echo "Cleaning up: $file"
    
    # Remove everything after the last proper closing script tag and before </body>
    # This will remove any duplicate or malformed content
    
    # First, let's find where the proper content should end
    # We want to keep everything up to the first proper downloadHTML function and bottom nav
    
    # Create a temporary file with the cleaned content
    temp_file=$(mktemp)
    
    # Extract the filename without extension for the download name
    filename=$(basename "$file" .html)
    
    # Use awk to clean up the file
    awk '
    BEGIN { 
        in_script = 0
        script_count = 0
        found_bottom_nav = 0
    }
    
    /function downloadHTML\(\) {/ {
        if (script_count == 0) {
            in_script = 1
            script_count++
            print
            next
        }
    }
    
    in_script && /^  }$/ {
        in_script = 0
        print
        next
    }
    
    /<!-- Bottom Navigation -->/ {
        if (found_bottom_nav == 0) {
            found_bottom_nav = 1
            print
            next
        }
    }
    
    found_bottom_nav && /<\/body>/ {
        print
        exit
    }
    
    in_script || found_bottom_nav || script_count == 0 {
        print
    }
    ' "$file" > "$temp_file"
    
    # Replace the original file with the cleaned version
    mv "$temp_file" "$file"
    
    echo "Cleaned up: $file"
done

echo "All templates cleaned up!"
