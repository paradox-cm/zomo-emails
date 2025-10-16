#!/usr/bin/env python3
"""
Script to update download pages to use Vercel URLs for icons instead of Material Icons font.
The download pages contain HTML-encoded content that needs to be updated.
"""

import os
import re
import glob

# Base URL for the Vercel deployment
BASE_URL = "https://zomo-emails.vercel.app"

# Mapping of Material Icon names to their SVG file paths
icon_mapping = {
    "handshake": "assets/images/icons/handshake.svg",
    "business": "assets/images/icons/business.svg", 
    "new_releases": "assets/images/icons/new_releases.svg",
    "person": "assets/images/icons/person.svg",
    "emoji_events": "assets/images/icons/emoji_events.svg",
    "health_and_safety": "assets/images/icons/health_and_safety.svg",
    "security": "assets/images/icons/security.svg",
    "speed": "assets/images/icons/speed.svg",
    "integration_instructions": "assets/images/icons/integration_instructions.svg",
    "favorite": "assets/images/icons/favorite.svg",
    "trending_up": "assets/images/icons/trending_up.svg",
    "article": "assets/images/icons/article.svg",
    "linkedin": "assets/images/icons/linkedin.svg",
    "download": "assets/images/icons/download.svg",
    "arrow_back": "assets/images/icons/arrow_back.svg",
    "monitor": "assets/images/icons/monitor.svg",
    "keyboard_arrow_down": "assets/images/icons/keyboard_arrow_down.svg",
    "light_mode": "assets/images/icons/light_mode.svg",
    "dark_mode": "assets/images/icons/dark_mode.svg"
}

def create_icon_img_tag_encoded(icon_name, style_attrs=""):
    """
    Create an HTML-encoded img tag for the icon with proper styling
    """
    if icon_name not in icon_mapping:
        print(f"⚠️  Warning: No local icon found for '{icon_name}'")
        return f'&lt;span class=&quot;material-icons&quot; {style_attrs}&gt;{icon_name}&lt;/span&gt;'
    
    svg_path = f"{BASE_URL}/{icon_mapping[icon_name]}"
    
    # Extract style attributes from the original span
    style_match = re.search(r'style=&quot;([^&]*)&quot;', style_attrs)
    if style_match:
        original_style = style_match.group(1)
        # Convert font-size to width/height for img tag
        width_height = "16px"  # default
        if "font-size:24px" in original_style:
            width_height = "24px"
        elif "font-size:32px" in original_style:
            width_height = "32px"
        elif "font-size:12px" in original_style:
            width_height = "12px"
        
        # Preserve color and other important styles
        color_match = re.search(r'color:([^;]+)', original_style)
        color = color_match.group(1) if color_match else "currentColor"
        
        # Create new style for img tag
        new_style = f'width:{width_height}; height:{width_height}; vertical-align:middle; color:{color};'
        
        # Add margin if present
        margin_match = re.search(r'margin-right:([^;]+)', original_style)
        if margin_match:
            new_style += f' margin-right:{margin_match.group(1)};'
    else:
        new_style = "width:16px; height:16px; vertical-align:middle;"
    
    return f'&lt;img src=&quot;{svg_path}&quot; alt=&quot;{icon_name}&quot; style=&quot;{new_style}&quot;&gt;'

def update_download_page(file_path):
    """
    Update a single download page to use local icons
    """
    print(f"📝 Updating {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match HTML-encoded Material Icons spans
        # Matches: &lt;span class=&quot;material-icons&quot; style=&quot;...&quot;&gt;icon_name&lt;/span&gt;
        pattern = r'&lt;span class=&quot;material-icons&quot;([^&]*)&gt;([^&]+)&lt;/span&gt;'
        
        def replace_icon(match):
            style_attrs = match.group(1)
            icon_name = match.group(2).strip()
            
            # Skip if it's not a known icon
            if icon_name not in icon_mapping:
                return match.group(0)  # Return original
            
            return create_icon_img_tag_encoded(icon_name, style_attrs)
        
        # Replace all Material Icons with local SVG images
        content = re.sub(pattern, replace_icon, content)
        
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
    print("🔄 Updating download pages to use Vercel URLs for icons...")
    print(f"Base URL: {BASE_URL}")
    print()
    
    # Find all newsletter download page files
    download_files = glob.glob("download-pages/zomo-health-*-template-download.html")
    
    if not download_files:
        print("❌ No newsletter download files found")
        return
    
    updated_count = 0
    
    for download_file in download_files:
        if update_download_page(download_file):
            updated_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully updated {updated_count} download page files")
    print()
    print("Icon URLs now point to:")
    print(f"{BASE_URL}/assets/images/icons/[icon_name].svg")
    print()
    print("Next steps:")
    print("1. Test the updated download pages")
    print("2. Verify that icons display correctly in the HTML code")
    print("3. Commit the changes to git")

if __name__ == "__main__":
    main()
