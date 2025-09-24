# Django Project Management Challenge

## Problem Description

[cite_start]This project requires implementing several simple Django models for a project management system[cite: 2]. The models to be completed are **Project**, **Category**, **RoleType**, and **Membership**.

### Required Models:

- [cite_start]**`Project`**: This model should have fields for `title`, `description`, `created_at`, `updated_at`, and a many-to-many relationship with the **`User`** model through a custom **`Membership`** model[cite: 48, 51]. [cite_start]It also needs a foreign key to **`Category`**[cite: 53].
- [cite_start]**`Category`**: This model includes a `name` field and a `parent` foreign key that links to itself[cite: 56, 58].
- [cite_start]**`RoleType`**: This model is implemented as an `IntegerChoices` field, defining roles as `"MEMBER"` (normal access) and `"OWNER"` (management access)[cite: 59, 61, 64].
- [cite_start]**`Membership`**: This model has foreign keys to **`User`** (`person`) and **`Project`** (`project`), plus an integer field for `role` from the `RoleType` model[cite: 67, 68, 69, 70]. [cite_start]The `person` and `project` fields together must be unique[cite: 94].

### Serializer and View Requirements:

- [cite_start]**`ProjectSerializer`**: This serializer must include `title`, `description`, `category`, `members`, `created_at`, and `updated_at` fields[cite: 72, 76, 77, 78, 79, 80, 81].
- **`ProjectListView`**: This view should provide a list of projects. [cite_start]It uses Django REST Framework's `ListAPIView` and is only accessible to authenticated users (`IsAuthenticated`)[cite: 82, 83, 85, 87]. [cite_start]It should return all projects stored in the database [cite: 88][cite_start], using the `ProjectSerializer` to format the data into JSON[cite: 89, 90]. [cite_start]The projects must be ordered by the last update time (`updated_at`)[cite: 95].

---

## Current Status

I have implemented the code for this challenge and received a score of **66 out of 100**. This score indicates that some of the requirements are not fully met. The issue might be related to the model relationships, serializer configuration, or the view's filtering and ordering.

---

## Seeking Assistance

I am looking for guidance and help to achieve a perfect score. If you have a solution or can help improve my code, I would greatly appreciate it if you could share your approach via a **Pull Request** or an **Issue**.
