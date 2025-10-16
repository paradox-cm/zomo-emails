#!/usr/bin/env python3
"""
Script to update email templates to use Vercel URL for icons instead of local paths.
Email clients need remote URLs to load images, not local file paths.
"""

import os
import re
import glob

# Base URL for the Vercel deployment
BASE_URL = "https://zomo-emails.vercel.app"

def update_icon_urls(file_path):
    """
    Update icon URLs in a template file to use the Vercel URL
    """
    print(f"🌐 Updating icon URLs in {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match local icon paths and replace with Vercel URL
        # Matches: src="assets/images/icons/icon_name.svg"
        pattern = r'src="assets/images/icons/([^"]*\.svg)"'
        
        def replace_with_vercel_url(match):
            icon_filename = match.group(1)
            return f'src="{BASE_URL}/assets/images/icons/{icon_filename}"'
        
        # Replace all local icon paths with Vercel URLs
        content = re.sub(pattern, replace_with_vercel_url, content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated {file_path}")
            return True
        else:
            print(f"ℹ️  No changes needed for {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    print("🌐 Updating email templates to use Vercel URLs for icons...")
    print(f"Base URL: {BASE_URL}")
    print()
    
    # Find all HTML template files
    template_files = glob.glob("emails/newsletters/*.html")
    
    if not template_files:
        print("❌ No template files found")
        return
    
    updated_count = 0
    
    for template_file in template_files:
        if update_icon_urls(template_file):
            updated_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully updated {updated_count} template files")
    print()
    print("Icon URLs now point to:")
    print(f"{BASE_URL}/assets/images/icons/[icon_name].svg")
    print()
    print("Next steps:")
    print("1. Deploy the icons to Vercel")
    print("2. Test the updated templates in Gmail")
    print("3. Verify that icons load correctly from remote URLs")

if __name__ == "__main__":
    main()
