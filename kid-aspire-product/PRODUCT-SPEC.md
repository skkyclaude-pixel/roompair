# Product Specification: Hybrid Voice Story Player

## Product Name: [TBD]
## Version: 0.1 (Draft)

---

## 1. Product Overview

A screen-free audio player for children (ages 3-10) that combines two features:

1. **Anyone Can Read** — Parents, grandparents, siblings record their voice reading any book. Child selects who reads to them at story time.
2. **Interactive Adventures** — Child talks to the speaker and chooses how the story unfolds.

**Mission:** Replace screen time with imaginative, personalized storytelling that keeps parents involved.

---

## 2. Target Market

| Segment | Description |
|---------|-------------|
| **Primary买家** | Parents of 3-10 year olds, £60-120k household income |
| **Secondary买家** | Grandparents (gift-givers) |
| **Geographic** | UK first, then EU, then US |
| **Kid age range** | 3-10 years old |

---

## 3. Core Features

### 3.1 Voice Recording (Anyone Can Read)
- Parent downloads app (iOS/Android)
- Parent selects book (from library or scans ISBN)
- Parent records themselves reading (page by page or continuous)
- Recording syncs to child's device via WiFi
- Child sees list of "Readers" (Mummy, Daddy, Grandma, etc.)
- Child taps reader → story plays with that voice

### 3.2 Interactive Stories (Adventure Mode)
- Child taps "Adventure" on device
- Device listens for voice commands ("I want to go left!", "Let's fight the dragon!")
- LLM generates next part of story based on choice
- Audio plays back through speaker
- LED lights indicate when device is listening

### 3.3 Hardware
- Simple speaker unit (no screen)
- Physical controls: Play/Pause, Volume, Mic On/Off
- LED ring for status (listening, playing, processing)
- WiFi for streaming/syncing
- Battery: 8-10 hours playback
- Materials: Soft-touch silicone shell, child-safe plastics

---

## 4. User Journey

### For Parents (setup)
1. Unbox device, download app
2. Connect device to home WiFi via app
3. Create parent account
4. Add child profile
5. Record first book OR browse story library

### For Kids (daily use)
1. Press "Play" to start
2. Choose mode: "Story" (recorded voice) or "Adventure" (interactive)
3. If Story: Choose who reads
4. If Adventure: Talk to choose what happens
5. Press "Pause" when done

---

## 5. Technical Architecture

### Hardware
- **SoC:** ESP32 or similar WiFi MCU
- **Speaker:** 3W mono speaker, 40mm driver
- **Microphone:** Dual MEMS mics, noise reduction
- **Battery:** 2000mAh LiPo
- **LED:** RGB ring (12 LEDs)

### Firmware
- **OTA updates** via WiFi
- **Local storage:** 4GB SD card for cached stories
- **Audio codec:** MP3, Opus

### Cloud/Backend
- **Auth:** Firebase Auth
- **Database:** Firestore (user data, book metadata)
- **Storage:** AWS S3 (audio files)
- **AI:** OpenAI API (for interactive stories) + ElevenLabs (TTS for pre-recordings)

### App
- **Framework:** React Native or Flutter
- **Features:** Recording, playback, library management, child profile

---

## 6. Content Strategy

### Phase 1: AI-Generated Interactive Stories
- 20-50 stories generated via LLM + TTS
- Categories: Fantasy, Adventure, Mystery, Bedtime
- Age-appropriate vocabulary (3-5, 6-8, 9-10)

### Phase 2: User-Recorded Books
- Parents record their own
- Public domain books included (free)
- Partnership with children's publishers (licensing deals)

### Phase 3: Premium Content
- Professional voice actors
- Branded stories (Disney, Pixar — licensing required)
- Subscription model for unlimited stories

---

## 7. Pricing Model

| Tier | Price | What's Included |
|------|-------|-----------------|
| **Device only** | £89 | Speaker hardware, 5 free interactive stories |
| **Starter Pack** | £119 | Device + 10 recorded stories (parents' choice) |
| **Subscription** | £7.99/mo | Unlimited interactive stories, new releases |
| **Gift Card** | £30-100 | Credit toward device or content |

---

## 8. MVP Roadmap

| Phase | Timeline | Deliverables |
|-------|----------|--------------|
| **Prototype** | Months 1-2 | Raspberry Pi + speaker + mic, basic voice interaction test |
| **MVP** | Months 3-6 | Working hardware + app + 10 interactive stories |
| **Beta** | Months 7-8 | 50 units to test families |
| **Launch** | Month 9 | Public launch, UK-focused |

---

## 9. Competitors

| Competitor | Strength | Weakness |
|------------|----------|----------|
| **Yoto** | Brand recognition, content library | No voice recording, no interactivity |
| **Tonies** | Character-based engagement | No custom voices, expensive content |
| **Echo Dot Kids** | Cheap, available | Not purpose-built, screen-adjacent |
| **Your Product** | Personal voice + interactivity | New brand, requires content creation |

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Voice recognition fails for kids | High | Medium | Extensive testing, child-specific acoustic models |
| Content costs spiral | Medium | High | AI-generated first, human only for premium |
| Yoto/Tonies add voice recording | Medium | High | Speed to market, focus on emotional hook |
| Hardware delays | High | High | Multiple manufacturer backups, prototype early |

---

## 11. Team Needs (Early Stage)

| Role | Skills Needed | Can Outsource? |
|------|---------------|----------------|
| **Hardware Engineer** | Audio, embedded systems | Yes (Shenzhen) |
| **Firmware Dev** | ESP32, C++ | Yes |
| **App Dev** | React Native / Flutter | Yes |
| **AI/ML Engineer** | STT, TTS, LLM | Yes (contractor) |
| **Children's Writer** | Story writing | Yes |
| **Founder** | Everything else | — |

---

## 12. Financial Model (Unit Economics)

### Revenue Streams
| Stream | Price | COGS | Margin |
|--------|-------|------|--------|
| Hardware (speaker) | £89 | £30 | 66% |
| Interactive story (one-off) | £9 | £0.50 (server) | 94% |
| Monthly subscription | £7.99/mo | £3/mo server + content | 62% |

### Unit Economics at Scale (Year 2)
| Metric | Conservative | Optimistic |
|--------|--------------|-------------|
| Units sold | 2,000 | 5,000 |
| Average revenue per unit | £120 (hardware + 1yr sub) | £180 (hardware + 2yr sub) |
| COGS per unit | £38 | £35 |
| Gross margin | 68% | 81% |
| CAC (marketing) | £30 | £25 |
| LTV | £150 | £220 |
| LTV:CAC | 5:1 | 8.8:1 |

### Break-Even Analysis
- **Prototype phase:** £50k (MVP)
- **Seed round needed:** £90k (to launch)
- **Months to break-even:** 18-24 months post-launch
- **Runway after launch:** 12 months

### Cost Structure (Monthly, Post-Launch)
| Item | Cost |
|------|------|
| Cloud/infrastructure | £2,000 |
| Content licensing/production | £3,000 |
| Customer support | £1,500 |
| Marketing (digital) | £5,000 |
| **Total** | **£11,500/mo** |

### Required to Break Even
- **Monthly recurring revenue (MRR):** £11,500
- **Equivalent subscribers:** ~1,440 (£7.99/mo)
- **Or equivalent hardware + content:** ~130 units/month at £89

---

*Last updated: 2026-04-28*