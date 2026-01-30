import re

# Read the HTML file
with open('Home.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Define the replacements
replacements = {
    'href="/city-tour"': 'href="Home-Pages/city-tour.html"',
    'href="/island-tour"': 'href="Home-Pages/island-tour.html"',
    'href="/accommodation"': 'href="accommodation/accommodation.html"',
    'href="/accommodation/"': 'href="accommodation/"',
    'href="/service"': 'href="Pages/Other Pages/service.html"',
    'href="/service-details"': 'href="Pages/Other Pages/service-details.html"',
    'href="/about-us"': 'href="Pages/Other Pages/about-us.html"',
    'href="/about-us-02"': 'href="Pages/Other Pages/about-us.html"',
    'href="/hotel-staff"': 'href="Pages/Other Pages/hotel-staff.html"',
    'href="/hotel-staff-02"': 'href="Pages/Other Pages/hotel-staff.html"',
    'href="/terms-conditions"': 'href="Pages/Other Pages/terms-conditions.html"',
    'href="/privacy-policy"': 'href="Pages/Other Pages/privacy-policy.html"',
    'href="/purchase-guide"': 'href="Pages/Other Pages/purchase-guide.html"',
    'href="/404"': 'href="Pages/Other Pages/404.html"',
    'href="/coming-soon"': 'href="Pages/Other Pages/coming-soon.html"',
    'href="/pricing-plan"': 'href="Pages/Other Pages/pricing-plan.html"',
    'href="/wishlist"': 'href="Pages/Other Pages/wishlist.html"',
    'href="/contact"': 'href="Pages/Other Pages/contact.html"',
    'href="/contact-2"': 'href="Pages/Other Pages/contact.html"',
    'href="/contact-3"': 'href="Pages/Other Pages/contact.html"',
    'href="/activity-1"': 'href="Pages/Our Activities/activity-1.html"',
    'href="/activity-2"': 'href="Pages/Our Activities/activity-2.html"',
    'href="/urban-city-stay"': 'href="Pages/Our Activities/urban-city-stay.html"',
    'href="/dining-experiences"': 'href="Pages/Our Activities/dining-experiences.html"',
    'href="/restaurant-details"': 'href="Pages/Our Activities/restaurant-details.html"',
    'href="/food-menu"': 'href="Pages/Our Activities/food-menu.html"',
    'href="/nightlife-tour"': 'href="Pages/Our Activities/nightlife-tour.html"',
    'href="/mountain-adventure"': 'href="Pages/Our Activities/mountain-adventure.html"',
    'href="/wellness-retreats"': 'href="Pages/Our Activities/wellness-retreats.html"',
    'href="/spa-menu"': 'href="Pages/Our Activities/spa-menu.html"',
    'href="/honeymoon-paradise"': 'href="Pages/Our Activities/honeymoon-paradise.html"',
    'href="/romantic-tour"': 'href="Pages/Our Activities/romantic-tour.html"',
    'href="/wildlife-safari"': 'href="Pages/Our Activities/wildlife-safari.html"'
}

# Apply all replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Write the updated content back to the file
with open('Home.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Navigation links have been fixed!")