# Creative Direction — Møns Klint Gift Site

*Senior interaction design review. Written before any new code is touched.*

---

## The single most important missing interaction: the arrival

The most important thing this site doesn't have yet is the arrival moment.

Right now, someone opens an envelope, scans a QR code, and the page loads. That transition — from a physical object held in their hands to a screen — is an interruption. The site needs to meet them in that gap and slow time down before it says anything.

**How it works:**

The page loads completely black. Not dark — black. No stars, no text, nothing. After 400ms, a single point of light appears in the exact center of the viewport. It grows slowly, the way your eyes adjust when you walk outside on a clear night. Stars resolve out of the darkness one at a time, spreading from that center point outward, over about 2.5 seconds. During this, no text, no UI. Then one line appears in small uppercase:

> "For [Sister] & [Partner]."

A beat — 1.2 seconds. Then the cliff silhouette rises from the bottom. Then "Møns Klint" in the display font, very large.

The whole arrival takes five seconds. But those five seconds do the most important work on the site: they close the door on wherever the recipients just were and open the door to somewhere else. Without them, the QR code is just a link. With them, scanning the code becomes the gesture of opening something.

---

## On the dark→light→dark arc

The structure is correct but the reason needs to be deliberate, not just atmospheric.

The dark hero isn't "mood" — it's Møns Klint specifically, because the extraordinary thing about this place is not the cliffs in daylight. Every Danish travel site has photos of the cliffs in daylight. What makes Møns Klint genuinely remarkable is that it's one of Europe's darkest skies. You stand on the clifftop at night and the Milky Way is visible. **That is the gift within the gift.**

The narrative: you arrive in the dark (standing on the cliff at night) → the warmth of day opens as the gift reveals itself → you return to dark at the end, because that's where the site began and that's what they're going back to when they actually take the trip.

The footer isn't just a footer — it's the promise of the night sky they'll stand under.

**The transition needs work.** Right now it's a hard cut to cream. It should feel like dawn — the cliffs catching first light. Technically: a narrow gradient band between the hero and reveal section, the cream bleeding up from the bottom of the cliff silhouette over ~80px. One CSS gradient. But the conceptual shift is everything.

---

## Visual identity: what Møns Klint suggests

**Palette refinements:**

- Chalk isn't white — it's warm off-white with a slight yellow-grey cast, almost old paper. The current `#faf9f7` cream is close.
- The hero sky should be more specifically the sky over Møns at night: deep indigo-black, something like `#07081a`. Not just dark — a colour.
- The Baltic in the right light is a dark blue-green distinctive to this sea — not Mediterranean turquoise, not North Sea grey. Around `#0d2b22`. Doesn't need to dominate, but if it appears once — in the cliff silhouette gradient, in a single line of text — it grounds the site in a specific geography.

**Typography:**

Qwitcher Grypen is right for display — romantic without being fussy. Body text moves too fast. Møns Klint has the quality of geological time — the chalk contains 70-million-year-old fossils. The prose should feel unhurried:
- Line-height on body copy → 1.85
- Letter-spacing on uppercase labels → another +0.05em
- Secondary text font-size → slightly smaller

The page should read the way the cliffs look: like something that has been there longer than you and will be there after you leave.

---

## The one thing that makes everything else feel intentional

**The cliff silhouette.**

Right now it's a generic SVG approximation of a cliff. The actual skyline of Møns Klint is specific and recognizable — there's a particular shape to the highest point, Dronningestolen, that anyone who's been there knows.

If that silhouette is traced to match the actual profile of the cliffs (not a generic "cliffs" shape), the whole hero shifts. It stops being a website about a cliff and becomes a website about *this cliff*. When the recipients arrive for the trip and walk to the viewpoint, they'll see exactly the shape they saw on the website. That moment of recognition — digital and physical colliding again — is what makes a gift feel designed rather than bought.

---

## Section-by-section audit

### Hero + star field — earning its place ✓
Completely. The Dark Sky Park angle is the strongest conceptual hook. Keep everything. The star field should be very subtle after arrival — barely perceptible twinkling, not distracting shimmer.

### Personal message + reveal section — earning its place ✓
This is the heart of the gift. The who's-going list earns its place too, especially because this is a group trip and naming the baby specifically is the detail that makes it feel like a human gesture, not a booking.

### Four-card "The Place" section — not earning its place as-is ✗
"White Cliffs," "Dark Sky Reserve," "Coastal Trails," "Slow Days" — these are brochure headings. They could be on any tourism site for any coastal destination in Northern Europe. The format (four equal cards with icons) suggests Wikipedia, not intimacy.

**Fix:** Replace the cards with four sentences of specific prose. No card UI, no icons, no headers. Tell it through the lens of *why this specific group will love it*:
- The baby will see the sea for the first time.
- You can pick 70-million-year-old belemnites out of the chalk face with your fingers.
- On the walk down to Hvideklint there's a point where the sea appears suddenly below you and it stops you in your tracks every time.
- On a clear night, the Milky Way.

Specific language. The place, not the category.

### Countdown / details section — conditionally earns its place
The countdown is right as a *feature* but it shouldn't be prominent until it has something real to count. "Dates coming soon" is a letdown in a gift context. Until dates are set, the section should just say "A weekend in [Month] [Year]" in large display type, beautifully typeset. The countdown appears when there's something to count.

### Polaroid wall — does not earn its place ✗
This is the biggest problem on the site. An empty frame is the wrong metaphor for anticipation — it describes absence, not possibility. A polaroid is a *result*. Showing six empty ones says "this thing hasn't happened and here is the void where the memories will go." That is not the feeling a gift reveal should end on.

**Fix:** Remove the polaroid wall entirely. Replace it with a single section — no label, no heading — just a prose passage that sets the scene of what they'll find when they get there. Not facts. Sensation:

> The chalk is so white it almost glows. The sea is the specific blue-green of the Baltic in August. You can hear it before you see it.

Give them something to imagine, not an empty frame to fill in later. After the trip, this section gets replaced — not filled in, replaced — with actual photos and past-tense language. We do that together when the time comes.

---

## Motion and scroll

The current fade-slide-in on scroll is a default pattern. It doesn't mean anything here — it's just "things appear as you scroll," which every site does.

**What Møns Klint actually feels like:** stillness, then sudden revelation. You walk through beech forest, emerge at the clifftop, and the entire Baltic is below you. The motion model should match: long pauses of stillness interrupted by a single clear event, not a continuous stream of things appearing at even intervals.

**Specific changes:**
- Increase all transition durations to 900ms
- Remove the `translateY` transform from most section reveals — keep only opacity. Sliding up is generic. Let them simply appear.
- Stagger cards (if cards remain) by 150ms so they read as a sequence
- The hero should be completely still after arrival. Stillness on a website is harder to achieve than motion and it communicates confidence.

**One deliberate moment of delight:**
At the exact moment you scroll past the cliff edge — the dark-to-light transition — a single, very faint horizontal shimmer crosses the page over 700ms. Like a wave, like a breath, like crossing a threshold. It never repeats. It exists to confirm that you've arrived somewhere, not to demonstrate that scroll detection works.

---

## What this site should never do

**No stock photography.** If an image appears on this site it must be a photo from someone who was there — you, the recipients, anyone in the group. A Getty image of Møns Klint puts the site in the same category as a travel agent's brochure. If you have no photos of the cliffs yet, use none. The site is stronger with no images than with the wrong ones.

**Don't name the feeling before they've had it.** "Slow Days" presumes what they'll feel. "Coastal Trails" describes an activity they might not choose. Describe the place. Let them have their own feeling.

**Don't be comprehensive.** The four-card section tries to cover all angles of the destination. The best gift reveals one angle so precisely that everything else comes as a surprise. The dark sky is that angle. Every design decision should be an approach toward that one thing.

**Don't use the word "adventure." Don't use "explore."** Test: could this sentence appear on a trail running brand's Instagram? If yes, cut it.

**Don't animate things that are working by being still.** The stars twinkling is enough.

---

## Priority order for implementation

1. **Build the arrival sequence** — black → single point of light → stars resolve → dedicatory line → cliff silhouette rises → title. This is the most important thing on the site and it doesn't exist yet.

2. **Replace the polaroid wall** with a prose passage evoking the place — sensation, not logistics.

3. **Rewrite "The Place"** as specific prose paragraphs — no card UI, no icons.

4. **Refine the cliff silhouette** to match the actual profile of Dronningestolen.

5. **Add the threshold shimmer** at the dark-to-light transition.

Everything else is already working.
