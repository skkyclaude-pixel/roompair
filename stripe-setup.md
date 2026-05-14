# Stripe Setup Guide

## Step 1: Create Stripe Account
1. Go to [stripe.com](https://stripe.com) and sign up
2. Verify your email and complete business details

## Step 2: Create a Payment Link
1. In Stripe Dashboard → **Products** → **Create Product**
2. Name: "30-min Style Consultation"
3. Price: £50 (enter as 5000 in pence)
4. Save

3. In Stripe Dashboard → **Payment Links** → **Create**
4. Select the product you just created
5. Copy the payment link URL

## Step 3: Add to Your Landing Page

Replace the `#` in the "Book Now" buttons with your Stripe link:

```html
<a href="https://buy.stripe.com/your-link-here" class="stylist-btn">Book Now</a>
```

Or use a single link for all:

```html
<a href="https://buy.stripe.com/your-link-here" class="btn">Book Your Consultation</a>
```

---

## Alternative: Use Calendly + Stripe

If you want to handle scheduling + payments together:

1. Create a Calendly account
2. Set up a paid event type (30 min, £50)
3. Connect Stripe inside Calendly (Integrations → Stripe)
4. Use your Calendly link in the HTML instead

---

## Quick Template (replace XXX with your links)

**HTML change:**
```html
<!-- For @redthreaadhome -->
<a href="https://buy.stripe.com/XXX" class="stylist-btn">Book Now</a>

<!-- Main CTA -->
<a href="https://buy.stripe.com/XXX" class="btn">Book Your Consultation</a>
```

---

## What's Next?

Once you have your Stripe link, I can update the HTML file with the real URLs. Just paste the link here!