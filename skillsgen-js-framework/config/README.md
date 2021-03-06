# ksa-matrix-widget

## Overview
The KSA Generator is driven primarily by a single CSV file used to generate a valid JSON file for consumption by Website API's and other applications that would find it useful.

### The *skillset.csv* file
#### Header Line
The first line in the `csv` file must contain the following :

```domain, parent, title, experience, proficiency, certifiable, agency, agency_url```

#### Field Descriptions

#### *domain* - `string`
The top-level "domain" to which a set of skill "categories" apply.

#### *parent* - `string`
The category (within the top-level "domain") to which a set individual skills apply.

#### *title* - `string`
Title of an individual skill.

#### *experience* - `integer`
A whole number value between 0 and 4 indicating a relatively objective measure of exposure and experience utilizing the skill.  The numbers generally represent the following amounts of experience:

- **1** - No direct experience, but a basic knowledge about what the skill signifies, or tools utilized
- **2** - Minimal experience. May have observed others performing tasks with the skill, or engaged in basic "tinkering"
- **3** - Basic experience.  May have used it for very minor projects.  Understand a limited amount of basic concepts well.
- **4** - Major experience.  Have used it for work, or significant projects.  Have a sold grasp of basic and intermediate usage.
- **5** - Highly Experienced.  Expertise at all levels, except for some advanced levels, of concepts and practice.

#### *proficiency* - `integer`
This is a subjective measure of self reported proficiency.  Generally a 100 point scale in increments of 10.  *NOTE: If the certifiable field is set to true, then the generator will use the `agency` and `agency_url` fields to set the proficiency level and generate URI links to the agency listed*

#### *certifiable* - `boolean`
If set to false, then the generator will not populate the "certificate" indication in the final output.  If set to true, a special indicator will be place on the skill, and a link to the certification will be generated using the `agency` and `agency_url` fields will be processed.

#### *agency* - `string`
The name of the certifying agency.  Should be `null` if `certifiable` is false.

#### *agency_url* - `string`
A valid URL for the certificate of certificate lookup form supplied by the authorized agency designated in the `agency` field.
