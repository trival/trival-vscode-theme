import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))

def invert_lightness(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    new_l = 1.0 - l
    r, g, b = colorsys.hls_to_rgb(h, new_l, s)
    return rgb_to_hex(r, g, b)

# Color mappings from dark to light
colors = {
    '#1F2528': None,  # editor.background
    '#cccfcb': None,  # editor.foreground
    '#151515': None,  # activityBar.background
    '#b3b3b3': None,  # sideBar.foreground
    '#090909': None,  # borders
    '#1F3a48': None,  # selections
    '#1F3a48cc': None,  # selection with alpha
    '#8393b6': None,  # line numbers
    '#1a1d20': None,  # menus/dropdowns
    '#2f393d': None,  # indent guides
    '#00000066': None,  # shadows with alpha
    '#0d070080': None,  # scrollbar bg with alpha
    '#c0c0c010': None,  # scrollbar hover with alpha
    # Syntax colors
    '#60606f': None,  # comments
    '#53cfcf': None,  # turquoise - keywords
    '#9dd076': None,  # green - strings
    '#da7cd7': None,  # purple - constants
    '#dab3f3': None,  # purple light - variables
    '#9cd7b6': None,  # turquoise light - parameters
    '#83a8ef': None,  # blue - types
    '#a6cef2': None,  # blue light - functions
    '#e0cb93': None,  # light orange - function declarations
    '#eeaf96': None,  # orange - macros
    '#f980aa': None,  # red - tags
    '#9a6fc8': None,  # dark purple - tag punctuation
}

print("Color conversions:")
for dark_hex in colors.keys():
    if 'cc' in dark_hex or '66' in dark_hex or '80' in dark_hex or '10' in dark_hex:
        # Handle colors with alpha
        base_color = dark_hex[:7]
        alpha = dark_hex[7:] if len(dark_hex) > 7 else ''
        light_hex = invert_lightness(base_color) + alpha
    else:
        light_hex = invert_lightness(dark_hex)
    colors[dark_hex] = light_hex
    print(f"{dark_hex} -> {light_hex}")

print("\nReady to paste mappings:")
for dark, light in colors.items():
    print(f"'{dark}': '{light}',")
