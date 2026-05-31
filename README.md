# Uni Relations

Übungsaufgabe: Modellierung eines Universitätssystems mit Django.

## Datenbankstruktur

```mermaid
erDiagram
    Student ||--|| StudentCard : "has (1:1)"
    Professor ||--o{ Course : "teaches (1:N)"
    Semester ||--o{ Course : "contains (1:N)"
    Course ||--|| CourseDescription : "has (1:1)"
    Student }o--o{ Course : "attends (M:N)"

    Student {
        int id PK
        string name
        string email
    }
    StudentCard {
        int id PK
        int student_id FK
        string card_number
    }
    Professor {
        int id PK
        string name
        string field_of_study
    }
    Semester {
        int id PK
        string name
    }
    Course {
        int id PK
        int professor_id FK
        int semester_id FK
        string title
    }
    CourseDescription {
        int id PK
        int course_id FK
        string description
    }
```