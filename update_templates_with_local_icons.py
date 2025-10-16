#!/usr/bin/env python3
"""
Script to update email templates to use local SVG icons instead of Material Icons font.
This fixes the issue where Gmail and other email clients don't support external font loading.
"""

import os
import re
import glob

# Directory containing email templates
templates_dir = "emails/newsletters"
icons_dir = "assets/images/icons"

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

def create_icon_img_tag(icon_name, style_attrs=""):
    """
    Create an img tag for the icon with proper styling
    """
    if icon_name not in icon_mapping:
        print(f"⚠️  Warning: No local icon found for '{icon_name}'")
        return f'<span class="material-icons" {style_attrs}>{icon_name}</span>'
    
    svg_path = icon_mapping[icon_name]
    
    # Extract style attributes from the original span
    style_match = re.search(r'style="([^"]*)"', style_attrs)
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
    
    # Clean up style_attrs to avoid conflicts - remove style attribute since we're adding our own
    clean_attrs = style_attrs.replace('style="', '').replace('"', '').strip()
    # Remove any remaining style-related attributes
    clean_attrs = re.sub(r'font-size:[^;]*;?', '', clean_attrs)
    clean_attrs = re.sub(r'vertical-align:[^;]*;?', '', clean_attrs)
    clean_attrs = re.sub(r'margin-right:[^;]*;?', '', clean_attrs)
    clean_attrs = re.sub(r'color:[^;]*;?', '', clean_attrs)
    clean_attrs = clean_attrs.strip()
    
    if clean_attrs:
        clean_attrs = f' {clean_attrs}'
    
    return f'<img src="{svg_path}" alt="{icon_name}" style="{new_style}"{clean_attrs}>'

def update_template_file(file_path):
    """
    Update a single template file to use local icons
    """
    print(f"📝 Updating {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match Material Icons spans
        # Matches: <span class="material-icons" style="...">icon_name</span>
        pattern = r'<span class="material-icons"([^>]*)>([^<]+)</span>'
        
        def replace_icon(match):
            style_attrs = match.group(1)
            icon_name = match.group(2).strip()
            
            # Skip if it's not a known icon
            if icon_name not in icon_mapping:
                return match.group(0)  # Return original
            
            return create_icon_img_tag(icon_name, style_attrs)
        
        # Replace all Material Icons with local SVG images
        content = re.sub(pattern, replace_icon, content)
        
        # Also remove the Material Icons font import and CSS
        content = re.sub(r'@import url\([^)]*Material\+Icons[^)]*\);', '', content)
        content = re.sub(r'<link[^>]*Material\+Icons[^>]*>', '', content)
        
        # Remove Material Icons CSS rules
        content = re.sub(r'\.material-icons\s*\{[^}]*\}', '', content)
        content = re.sub(r'\.material-icons[^{]*\{[^}]*\}', '', content)
        
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
    print("🔄 Updating email templates to use local SVG icons...")
    print()
    
    # Find all HTML template files
    template_files = glob.glob(os.path.join(templates_dir, "*.html"))
    
    if not template_files:
        print(f"❌ No template files found in {templates_dir}")
        return
    
    updated_count = 0
    
    for template_file in template_files:
        if update_template_file(template_file):
            updated_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Successfully updated {updated_count} template files")
    print()
    print("Next steps:")
    print("1. Test the updated templates in Gmail")
    print("2. Verify that icons display correctly")
    print("3. Check that the email layout still looks good")
    print("4. Commit the changes to git")

if __name__ == "__main__":
    main()
