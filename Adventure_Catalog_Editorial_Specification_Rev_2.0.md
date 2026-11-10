# AdventureFinder

# Adventure Catalog Editorial Specification

## Revision 2.0 --- Draft

**Status:** Draft\
**Date:** 2026-08-08

------------------------------------------------------------------------

## 1. Purpose

This specification defines the canonical schema and editorial rules for
the AdventureFinder Adventure Catalog.

The Adventure Catalog identifies discrete published adventures and
records their basic bibliographic and structural metadata.

The catalog is intentionally narrow. Its purpose is to establish **what
adventures exist and where they are located**.

The Adventure Catalog does **not** attempt to describe, score,
recommend, or evaluate what an adventure is like to play. Interpretive
AdventureFinder analysis belongs in separate data structures linked to
the catalog by **Adventure ID**.

------------------------------------------------------------------------

## 2. Canonical Schema

Every AdventureFinder catalog entry MUST contain the following fields,
in this order:

  -----------------------------------------------------------------------
  Field                               Purpose
  ----------------------------------- -----------------------------------
  Adventure ID                        Stable internal identity

  Adventure Title                     Human-readable identity

  Source Book                         Published source containing the
                                      adventure

  Book Publisher                      Publisher of the source book

  Start Page                          First page of the discrete
                                      adventure

  End Page                            Last page of the discrete adventure

  -----------------------------------------------------------------------

These fields constitute the canonical **initial catalog layer**.

Additional interpretive fields MUST NOT be added to the canonical
catalog merely because they are useful for search or recommendation.
Changes to the canonical schema require an explicit revision of this
specification.

------------------------------------------------------------------------

## 3. Core Catalog Principles

### 3.1 Stable Identity

Every discrete adventure receives a permanent **Adventure ID**.

The Adventure ID is the primary key connecting the catalog entry to any
future AdventureFinder analysis, evidence, recommendation, or other
derived data.

Once assigned, an Adventure ID MUST NOT be reassigned to a different
adventure.

### 3.2 Published Adventure Boundaries

Catalog entries represent discrete published adventures rather than
books as such.

A single source book MAY contain one adventure, multiple independent
adventures, multiple linked adventures, or other material that does not
constitute a catalogable adventure.

Adventure boundaries MUST therefore be determined editorially rather
than assumed from the product boundary.

### 3.3 Factual Catalog, Separate Analysis

The catalog SHOULD remain primarily bibliographic and structural.

The following types of information do not belong in the canonical
catalog layer:

-   Combat intensity
-   Exploration intensity
-   Roleplaying emphasis
-   Tactical complexity
-   Linearity
-   Player agency
-   Tone
-   Horror intensity
-   Puzzle emphasis
-   GM preparation burden
-   Beginner friendliness
-   Terrain fit
-   Writing quality
-   Encounter quality
-   Overall quality or recommendation scores

Such characteristics belong to the separate **AdventureFinder Analysis**
layer.

### 3.4 Preserve Provenance

Every cataloged adventure MUST retain a clear relationship to the
published source in which it appears and the publisher responsible for
that source.

------------------------------------------------------------------------

## 4. Field Definitions and Editorial Rules

### 4.1 Adventure ID

**Definition:** A permanent, unique AdventureFinder identifier assigned
to a discrete adventure.

**Format:**

`ADV-0001`

The numeric portion SHOULD use four digits with leading zeroes.

Examples:

-   `ADV-0001`
-   `ADV-0044`
-   `ADV-0122`

Once assigned, an Adventure ID MUST NOT be reused for another adventure,
even if the original catalog entry is later deprecated, merged, or
otherwise revised.

Subordinate identifiers MAY be introduced in future specifications when
a single adventure requires separately addressable structural units, but
such identifiers do not replace the parent Adventure ID.

------------------------------------------------------------------------

### 4.2 Adventure Title

**Definition:** The published title of the discrete adventure.

The title SHOULD preserve the publisher's title and normal
capitalization.

Minor normalization MAY be applied where necessary for consistent
catalog presentation, but editorial rewriting of titles SHOULD be
avoided.

For an adventure published as a standalone product, **Adventure Title**
and **Source Book** MAY be identical.

------------------------------------------------------------------------

### 4.3 Source Book

**Definition:** The published product or source containing the cataloged
adventure.

For anthology products, this identifies the containing book rather than
the individual adventure.

For standalone adventures, the Source Book MAY be identical to the
Adventure Title.

The title SHOULD be recorded consistently across all adventures drawn
from the same source.

------------------------------------------------------------------------

### 4.4 Book Publisher

**Definition:** The publisher responsible for the source book containing
the adventure.

Publisher names SHOULD use a consistent canonical form throughout the
catalog.

The Book Publisher field records publication provenance; it is not
intended to capture individual adventure authors, designers, editors,
licensors, or other credits.

Those forms of creator attribution MAY be represented elsewhere in
AdventureFinder in future specifications.

------------------------------------------------------------------------

### 4.5 Start Page

**Definition:** The first page belonging to the discrete adventure
within its source book.

The Start Page SHOULD identify the beginning of adventure-specific
content rather than general book-level front matter.

Determining the Start Page MAY require editorial judgment for
anthologies, campaign books, collections, or products with shared
introductory material.

Page references SHOULD correspond to the page-numbering convention
adopted for the source during cataloging and MUST be applied
consistently within that source.

------------------------------------------------------------------------

### 4.6 End Page

**Definition:** The final page belonging to the discrete adventure
within its source book.

The End Page SHOULD include adventure-specific appendices, handouts,
maps, or other supporting material when those materials are clearly part
of the discrete adventure.

Shared book-level appendices or reference material SHOULD NOT
automatically be included merely because they follow the adventure.

Determining the End Page MAY require editorial judgment.

------------------------------------------------------------------------

------------------------------------------------------------------------

## 5. Determining What Constitutes a Discrete Adventure

The fundamental cataloging unit is the **discrete playable adventure**,
not necessarily the commercial product.

A source book SHOULD receive multiple Adventure IDs when it contains
multiple adventures that can meaningfully be identified as distinct
playable works.

Relevant evidence MAY include:

-   Explicit adventure titles
-   Chapter or section boundaries
-   Separate premises or objectives
-   Distinct starting conditions
-   Distinct conclusions
-   Independent level recommendations
-   Separate expected play durations
-   Publisher presentation of the material as multiple adventures

A source SHOULD NOT be fragmented merely because it contains multiple
chapters, locations, encounters, quests, or acts.

Conversely, multiple adventures SHOULD NOT be collapsed into one catalog
entry merely because they are sold or bound together.

Ambiguous boundaries require editorial judgment.

------------------------------------------------------------------------

## 6. Catalog Boundary Principle

The Adventure Catalog answers questions such as:

-   What published adventures exist?
-   What is each adventure called?
-   Which source contains it?
-   Who published that source?
-   Where does the adventure begin and end?

The Adventure Catalog does **not** answer questions such as:

-   What is this adventure like to play?
-   How much combat or exploration does it contain?
-   How linear is it?
-   How much preparation does it require?
-   What tone does it have?
-   Who is likely to enjoy it?
-   How well designed is it?
-   How well does it fit a particular table, campaign, terrain
    collection, or player preference?
-   Should AdventureFinder recommend it?

Those questions belong to later AdventureFinder analysis and
recommendation layers.

This separation is intentional.

------------------------------------------------------------------------

## 7. Canonical Record Example

  --------------------------------------------------------------------------
  Adventure   Adventure   Source       Book          Start Page   End Page
  ID          Title       Book         Publisher
  ----------- ----------- ------------ ------------- ------------ ----------
  ADV-XXXX    Example     Example      Example                 10         42
              Adventure   Source Book  Publisher

  --------------------------------------------------------------------------

The example above illustrates schema and formatting only and does not
constitute a catalog record.

------------------------------------------------------------------------

## 8. Relationship to Future AdventureFinder Data

The Adventure Catalog is intended to function as the stable identity
layer beneath richer AdventureFinder systems.

Conceptually:

`Adventure ID → Catalog Record`

The same Adventure ID MAY subsequently connect to:

-   AdventureFinder analytical assessments
-   Evidence and provenance records
-   Semantic representations
-   Search indexes
-   Community-reported information
-   Creator or publisher metadata
-   Recommendation results
-   Editorial audit history

Those systems SHOULD reference the canonical Adventure ID rather than
duplicating or replacing catalog identity.

------------------------------------------------------------------------

## 9. Specification Authority and Revision Policy

This document governs the meaning and structure of the AdventureFinder
Adventure Catalog.

Changes to any of the following require a new revision of this
specification:

-   Canonical catalog fields
-   Field meanings
-   Adventure-boundary methodology
-   Catalog-versus-analysis boundaries

Existing catalog records MUST NOT silently change meaning when the
specification changes.

Where a methodological change materially affects existing records,
affected records SHOULD be reviewed or migrated explicitly.

Draft revisions SHOULD be clearly identified as drafts until accepted.

------------------------------------------------------------------------

## 10. LLM Application Guidance

When an LLM is used to create, review, or modify AdventureFinder catalog
records, it MUST treat this specification as normative.

The LLM SHOULD:

1.  Apply the canonical schema exactly.
2.  Distinguish source evidence from editorial inference.
3.  Avoid inventing unavailable bibliographic facts.
4.  Flag genuine ambiguity rather than silently resolving uncertain
    adventure boundaries.
5.  Preserve existing Adventure IDs.
6.  Keep interpretive AdventureFinder analysis outside the canonical
    catalog.
7.  Prefer explicit evidence from the published source over assumptions
    based on title, genre, reputation, or general knowledge.

When confidence is insufficient to establish a catalog field
responsibly, the field SHOULD be flagged for editorial review rather
than populated with an unsupported guess.

------------------------------------------------------------------------

## 11. Revision History

  --------------------------------------------------------------------------
  Revision          Date              Status            Description
  ----------------- ----------------- ----------------- --------------------
  2.0-draft         2026-08-08        Draft             Removes Sessions
                                                        and Levels from the
                                                        canonical Adventure
                                                        Catalog, establishing
                                                        a six-field catalog
                                                        schema focused on
                                                        stable identity,
                                                        publication
                                                        provenance, and
                                                        adventure boundaries.

  1.0-draft         2026-08-07        Draft             Initial
                                                        AdventureFinder
                                                        Adventure Catalog
                                                        Editorial
                                                        Specification.
                                                        Establishes the
                                                        canonical
                                                        eight-field catalog
                                                        schema,
                                                        adventure-boundary
                                                        principles,
                                                        normalized session
                                                        baseline,
                                                        catalog/analysis
                                                        separation, and LLM
                                                        application
                                                        guidance.

  --------------------------------------------------------------------------
