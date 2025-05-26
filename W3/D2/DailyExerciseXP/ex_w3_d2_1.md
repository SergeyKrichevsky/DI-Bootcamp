## Exercise 1: Identifying Data Types

Below is the classification of various data sources as structured or unstructured data:

1. **A company’s financial reports stored in an Excel file**  — **Structured Data**  
   *Reason: The data is organized in a tabular format with predefined columns and rows.*

2. **Photographs uploaded to a social media platform**  — **Unstructured Data**  
   *Reason: Image files do not follow a formal data model and are not stored in a tabular format.*

3. **A collection of news articles on a website**  — **Unstructured Data**  
   *Reason: Text data from articles is not structured into columns and rows.*

4. **Inventory data in a relational database**  — **Structured Data**  
   *Reason: Stored in tables with clear schema definitions and data types.*

5. **Recorded interviews from a market research study**  — **Unstructured Data**  
   *Reason: Audio files lack structured schema and require transcription for structured analysis.*


## Exercise 2: Transformation Exercise

Below are methods for converting unstructured data into structured formats, along with reasoning and potential applications.

---

### 1. A Series of Blog Posts About Travel Experiences

**Purpose of Structuring:**  
To extract and retrieve practical information for travel planning and content analysis.

**Proposed Method:**  
- Assign metadata to each post:
  - Location(s) mentioned
  - Author
  - Date of publication
  - Tags/topics (e.g., food, culture, transport)
- Use tags instead of fixed columns to accommodate multiple themes per post.
- Store structured data in a format like JSON or in a database with a many-to-many relationship between posts and tags.

**Example JSON Structure:**
```json
{
  "title": "My Journey to Kyoto",
  "author": "alex_traveler",
  "date": "2024-07-18",
  "location": "Japan, Kyoto",
  "tags": ["temples", "food", "urban culture"],
  "url": "https://example.com/blog/kyoto-trip"
}
```

### 2. Audio Recordings of Customer Service Calls

**Purpose of Structuring:**  
To analyze customer interactions for quality improvement, training, and customer satisfaction metrics.

**Proposed Method:**

1. **Transcription**  
   Convert audio recordings to text using speech recognition tools such as:
   - Whisper (OpenAI)
   - Google Speech-to-Text
   - Amazon Transcribe

2. **Usefulness of Structuring**  
   The transcription allows:
   - Searching for specific phrases or issues.
   - Labeling examples of effective and ineffective communication.
   - Identifying key conversation phases:
     - Understanding customer needs
     - Offering relevant solutions
     - Closing the sale
     - Creating a positive customer experience
     - Asking for feedback or referrals

3. **Structuring Key Elements**  
   - Tag calls by quality of service: “good”, “needs improvement”
   - Extract metadata:
     - Date and time
     - Duration
     - Agent name/ID
     - Customer name/ID (if available)
     - Topics discussed
     - Emotional tone
   - Segment conversation phases:
     - Greeting
     - Problem description
     - Solution offering
     - Closing
     - Follow-up

4. **Advanced Features (optional)**  
   - Compare conversations with predefined scripts and flag deviations.
   - Detect tone, politeness, and emotion using NLP tools.
   - Identify recurring pain points or service gaps.

**Example JSON Structure:**

```json
{
  "call_id": 1243,
  "date": "2024-12-03",
  "duration": "00:05:47",
  "agent": "Anna S.",
  "customer": "Ivan P.",
  "topic": ["billing", "refund"],
  "sentiment": "negative",
  "transcript": "Здравствуйте, мне не пришёл возврат средств за товар...",
  "audio_url": "https://example.com/calls/1243.mp3"
}
```

### 3. Handwritten Notes from a Brainstorming Session

**Purpose of Structuring:**  
To organize raw creative input from a brainstorming session into actionable, searchable, and evaluable information.

**Proposed Method:**

1. **Digitization**  
   Convert handwritten notes into digital text using:
   - Optical Character Recognition (OCR)
   - Manual transcription

2. **Categorization by Purpose**  
   - Group ideas based on the goals they aim to achieve.
   - If session goals are unknown, use thematic clustering to identify major idea groups (e.g., product, marketing, technical).

3. **Author Attribution**  
   - If available, tag ideas with the name or initials of the person who proposed them.

4. **Status Tracking (if applicable)**  
   - Mark which ideas were later considered useful, feasible, or were rejected.
   - If no post-analysis was done, store all ideas as-is for future processing.

5. **Advanced Structuring (optional):**
   - Link ideas to potential projects or objectives.
   - Use scoring systems to evaluate:
     - Feasibility (1–5)
     - Potential impact (1–5)
   - Create categories like:
     - Accepted
     - Under review
     - Deferred
     - Rejected

**Example JSON Structure:**
```json
{
  "idea": "Integrate referral program into onboarding flow",
  "author": "Elena",
  "goal": "Increase user acquisition",
  "status": "Accepted",
  "feasibility": 4,
  "impact": 5
}
```

### 4. A Video Tutorial on Cooking

**Purpose of Structuring:**  
To make the video more navigable, informative, and easy to use for learning or preparation.

**Proposed Method:**

1. **Transcription**  
   - Convert spoken content into text using automatic transcription tools.
   - Enables text-based search and step extraction.

2. **Timecodes for Video Chapters**  
   - Add timestamps to mark different stages of the recipe:
     - Introduction
     - Ingredients
     - Preparation steps
     - Cooking
     - Serving
   - Allows quick navigation to any part of the tutorial.

3. **Metadata Extraction**  
   - Title of the recipe
   - Short description of the dish
   - Author/creator
   - Duration
   - Cuisine type, difficulty level, preparation time

4. **Structured Lists**  
   - **Ingredients** (quantities included)
   - **Required tools/equipment** (e.g., blender, oven, specific utensils)

5. **Optional Enhancements:**  
   - **Tagging**: classify by cuisine, meal type (e.g., breakfast, dessert), diet (vegan, keto).
   - **Step extraction using NLP**:
     - Parse the transcript to extract actionable steps:
       - “Chop the onions”
       - “Boil water”
       - “Mix all ingredients”  
     - Useful for generating summaries or step-by-step guides automatically.

**Example JSON Structure:**
```json
{
  "title": "How to Make Vegan Lasagna",
  "author": "Chef Elena",
  "duration": "00:12:45",
  "description": "A step-by-step tutorial for a plant-based lasagna recipe.",
  "ingredients": [
    "1 zucchini",
    "200g tomato sauce",
    "250g tofu"
  ],
  "tools": ["oven", "baking dish", "knife"],
  "steps": [
    {"time": "00:30", "instruction": "Chop the zucchini"},
    {"time": "02:15", "instruction": "Preheat the oven"},
    {"time": "03:40", "instruction": "Mix tofu with seasoning"}
  ],
  "tags": ["vegan", "lasagna", "italian"],
  "video_url": "https://example.com/videos/vegan-lasagna"
}
```

