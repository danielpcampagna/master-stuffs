CREATE TABLE IF NOT EXISTS "accomplishments" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "enrollment_id" integer personal,
    "phase_id" integer indirect,
    "conclusion_date" date indirect,
    "obs" varchar(255) indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE sqlite_sequence(name, seq);

CREATE INDEX "index_accomplishments_on_enrollment_id" ON "accomplishments" ("enrollment_id");

CREATE INDEX "index_accomplishments_on_phase_id" ON "accomplishments" ("phase_id");

CREATE TABLE IF NOT EXISTS "advisement_authorizations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "professor_id" integer personal,
    "level_id" integer indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_advisement_authorizations_on_level_id" ON "advisement_authorizations" ("level_id");

CREATE INDEX "index_advisement_authorizations_on_professor_id" ON "advisement_authorizations" ("professor_id");

CREATE TABLE IF NOT EXISTS "advisements" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "professor_id" integer NOT NULL personal,
    "enrollment_id" integer NOT NULL personal,
    "main_advisor" boolean DEFAULT 0 indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_advisements_on_enrollment_id" ON "advisements" ("enrollment_id");

CREATE INDEX "index_advisements_on_professor_id" ON "advisements" ("professor_id");

CREATE TABLE IF NOT EXISTS "allocations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "day" varchar(255),
    "room" varchar(255),
    "start_time" integer,
    "end_time" integer,
    "course_class_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_allocations_on_course_class_id" ON "allocations" ("course_class_id");

CREATE TABLE IF NOT EXISTS "carrier_wave_files" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "medium_hash" varchar(255),
    "binary" blob,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "reference_counter" integer DEFAULT 0,
    "original_filename" varchar,
    "content_type" varchar,
    "size" integer
);

CREATE TABLE IF NOT EXISTS "cities" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "state_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_cities_on_state_id" ON "cities" ("state_id");

CREATE TABLE IF NOT EXISTS "class_enrollment_requests" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "enrollment_request_id" integer indirect,
    "course_class_id" integer,
    "class_enrollment_id" integer,
    "status" varchar DEFAULT 'Solicitada',
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL,
    "action" varchar DEFAULT 'Adição'
);

CREATE INDEX "index_class_enrollment_requests_on_class_enrollment_id" ON "class_enrollment_requests" ("class_enrollment_id");

CREATE INDEX "index_class_enrollment_requests_on_course_class_id" ON "class_enrollment_requests" ("course_class_id");

CREATE INDEX "index_class_enrollment_requests_on_enrollment_request_id" ON "class_enrollment_requests" ("enrollment_request_id");

CREATE TABLE IF NOT EXISTS "class_enrollments" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "obs" text indirect,
    "grade" integer,
    "situation" varchar(255),
    "course_class_id" integer,
    "enrollment_id" integer personal,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "disapproved_by_absence" boolean DEFAULT 0,
    "grade_not_count_in_gpr" boolean DEFAULT 0,
    "justification_grade_not_count_in_gpr" varchar DEFAULT ''
);

CREATE INDEX "index_class_enrollments_on_course_class_id" ON "class_enrollments" ("course_class_id");

CREATE INDEX "index_class_enrollments_on_enrollment_id" ON "class_enrollments" ("enrollment_id");

CREATE TABLE IF NOT EXISTS "class_schedules" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "year" integer,
    "semester" integer,
    "enrollment_start" datetime,
    "enrollment_end" datetime,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL,
    "enrollment_adjust" datetime,
    "enrollment_insert" datetime,
    "enrollment_remove" datetime
);

CREATE TABLE IF NOT EXISTS "countries" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "nationality" varchar DEFAULT '-'
);

CREATE TABLE IF NOT EXISTS "course_classes" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "course_id" integer,
    "professor_id" integer personal,
    "year" integer,
    "semester" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "not_schedulable" boolean DEFAULT 0,
    "obs_schedule" varchar
);

CREATE INDEX "index_course_classes_on_course_id" ON "course_classes" ("course_id");

CREATE INDEX "index_course_classes_on_professor_id" ON "course_classes" ("professor_id");

CREATE TABLE IF NOT EXISTS "course_research_areas" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "course_id" integer,
    "research_area_id" integer,
    "created_at" datetime,
    "updated_at" datetime
);

CREATE INDEX "index_course_research_areas_on_course_id" ON "course_research_areas" ("course_id");

CREATE INDEX "index_course_research_areas_on_research_area_id" ON "course_research_areas" ("research_area_id");

CREATE TABLE IF NOT EXISTS "course_types" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "has_score" boolean,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "schedulable" boolean DEFAULT 1,
    "show_class_name" boolean DEFAULT 1,
    "allow_multiple_classes" boolean DEFAULT 0 NOT NULL,
    "on_demand" boolean DEFAULT 0 NOT NULL
);

CREATE TABLE IF NOT EXISTS "courses" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "code" varchar(255),
    "content" text,
    "credits" integer,
    "course_type_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "workload" integer,
    "available" boolean DEFAULT 1
);

CREATE INDEX "index_courses_on_course_type_id" ON "courses" ("course_type_id");

CREATE TABLE IF NOT EXISTS "custom_variables" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "description" varchar(255),
    "variable" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "value" text
);

CREATE TABLE IF NOT EXISTS "deferral_types" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "description" varchar(255),
    "duration_semesters" integer DEFAULT 0,
    "phase_id" integer indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "duration_months" integer DEFAULT 0,
    "duration_days" integer DEFAULT 0
);

CREATE INDEX "index_deferral_types_on_phase_id" ON "deferral_types" ("phase_id");

CREATE TABLE IF NOT EXISTS "deferrals" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "approval_date" date indirect,
    "obs" varchar(255) indirect,
    "enrollment_id" integer personal,
    "deferral_type_id" integer indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_deferrals_on_deferral_type_id" ON "deferrals" ("deferral_type_id");

CREATE INDEX "index_deferrals_on_enrollment_id" ON "deferrals" ("enrollment_id");

CREATE TABLE IF NOT EXISTS "dismissal_reasons" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "description" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "show_advisor_name" boolean DEFAULT 0,
    "thesis_judgement" varchar(255)
);

CREATE TABLE IF NOT EXISTS "dismissals" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "date" date indirect,
    "enrollment_id" integer personal,
    "dismissal_reason_id" integer indirect,
    "obs" text indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_dismissals_on_dismissal_reason_id" ON "dismissals" ("dismissal_reason_id");

CREATE INDEX "index_dismissals_on_enrollment_id" ON "dismissals" ("enrollment_id");

CREATE TABLE IF NOT EXISTS "email_templates" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar,
    "to" varchar,
    "subject" varchar,
    "body" text,
    "enabled" boolean DEFAULT 1,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS "enrollment_holds" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "enrollment_id" integer personal,
    "year" integer indirect,
    "semester" integer indirect,
    "number_of_semesters" integer DEFAULT 1 indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "active" boolean DEFAULT 1 indirect
);

CREATE INDEX "index_enrollment_holds_on_enrollment_id" ON "enrollment_holds" ("enrollment_id");

CREATE TABLE IF NOT EXISTS "enrollment_request_comments" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "message" text indirect,
    "enrollment_request_id" integer indirect,
    "user_id" integer personal,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL
);

CREATE INDEX "index_enrollment_request_comments_on_enrollment_request_id" ON "enrollment_request_comments" ("enrollment_request_id");

CREATE INDEX "index_enrollment_request_comments_on_user_id" ON "enrollment_request_comments" ("user_id");

CREATE TABLE IF NOT EXISTS "enrollment_requests" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "year" integer indirect,
    "semester" integer indirect,
    "enrollment_id" integer personal,
    "last_student_change_at" datetime indirect,
    "last_staff_change_at" datetime indirect,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL,
    "student_view_at" datetime
);

CREATE INDEX "index_enrollment_requests_on_enrollment_id" ON "enrollment_requests" ("enrollment_id");

CREATE TABLE IF NOT EXISTS "enrollment_statuses" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "user" boolean
);

CREATE TABLE IF NOT EXISTS "enrollments" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL personal,
    "enrollment_number" varchar(255) personal,
    "student_id" integer personal,
    "level_id" integer personal,
    "enrollment_status_id" integer personal,
    "admission_date" date personal,
    "obs" text personal,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "thesis_title" varchar(255) personal,
    "thesis_defense_date" date personal,
    "research_area_id" integer personal
);

CREATE INDEX "index_enrollments_on_enrollment_status_id" ON "enrollments" ("enrollment_status_id");

CREATE INDEX "index_enrollments_on_level_id" ON "enrollments" ("level_id");

CREATE INDEX "index_enrollments_on_research_area_id" ON "enrollments" ("research_area_id");

CREATE INDEX "index_enrollments_on_student_id" ON "enrollments" ("student_id");

CREATE TABLE IF NOT EXISTS "institutions" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "code" varchar(255)
);

CREATE TABLE IF NOT EXISTS "levels" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "course_name" varchar(255),
    "default_duration" integer DEFAULT 0,
    "show_advisements_points_in_list" boolean,
    "short_name_showed_in_list_header" varchar
);

CREATE TABLE IF NOT EXISTS "majors" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "level_id" integer indirect,
    "institution_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_majors_on_institution_id" ON "majors" ("institution_id");

CREATE INDEX "index_majors_on_level_id" ON "majors" ("level_id");

CREATE TABLE IF NOT EXISTS "notification_logs" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "notification_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "to" varchar(255),
    "subject" varchar(255),
    "body" text,
    "attachments_file_names" varchar
);

CREATE INDEX "index_notification_logs_on_notification_id" ON "notification_logs" ("notification_id");

CREATE TABLE IF NOT EXISTS "notifications" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" varchar(255),
    "to_template" varchar(255),
    "subject_template" varchar(255),
    "body_template" text,
    "notification_offset" varchar(255),
    "query_offset" varchar(255),
    "frequency" varchar(255),
    "next_execution" datetime,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "individual" boolean DEFAULT 1,
    "query_id" integer NOT NULL,
    "has_grades_report_pdf_attachment" boolean DEFAULT 0
);

CREATE INDEX "index_notifications_on_query_id" ON "notifications" ("query_id");

CREATE TABLE IF NOT EXISTS "phase_completions" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "enrollment_id" integer personal,
    "phase_id" integer,
    "due_date" datetime,
    "completion_date" datetime,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_phase_completions_on_enrollment_id" ON "phase_completions" ("enrollment_id");

CREATE INDEX "index_phase_completions_on_phase_id" ON "phase_completions" ("phase_id");

CREATE TABLE IF NOT EXISTS "phase_durations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "phase_id" integer,
    "level_id" integer,
    "deadline_semesters" integer DEFAULT 0,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "deadline_months" integer DEFAULT 0,
    "deadline_days" integer DEFAULT 0
);

CREATE INDEX "index_phase_durations_on_level_id" ON "phase_durations" ("level_id");

CREATE INDEX "index_phase_durations_on_phase_id" ON "phase_durations" ("phase_id");

CREATE TABLE IF NOT EXISTS "phases" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "description" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "is_language" boolean DEFAULT 0,
    "extend_on_hold" boolean DEFAULT 0,
    "active" boolean DEFAULT 1
);

CREATE TABLE IF NOT EXISTS "professor_research_areas" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "professor_id" integer personal,
    "research_area_id" integer indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_professor_research_areas_on_professor_id" ON "professor_research_areas" ("professor_id");

CREATE INDEX "index_professor_research_areas_on_research_area_id" ON "professor_research_areas" ("research_area_id");

CREATE TABLE IF NOT EXISTS "professors" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL personal,
    "name" varchar(255) personal,
    "cpf" varchar(255) personal,
    "birthdate" date personal,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "sex" varchar(255) personal,
    "civil_status" varchar(255) personal,
    "identity_number" varchar(255) personal,
    "identity_issuing_body" varchar(255) personal,
    "identity_expedition_date" varchar(255) personal,
    "neighborhood" varchar(255) personal,
    "address" varchar(255) personal,
    "city_id" integer personal,
    "zip_code" varchar(255) personal,
    "telephone1" varchar(255) personal,
    "telephone2" varchar(255) personal,
    "siape" varchar(255) personal,
    "enrollment_number" varchar(255) personal,
    "identity_issuing_place" varchar(255) personal,
    "institution_id" integer personal,
    "email" varchar(255) personal,
    "academic_title_date" date personal,
    "academic_title_country_id" integer personal,
    "academic_title_institution_id" integer personal,
    "academic_title_level_id" integer personal,
    "obs" text personal,
    "user_id" integer personal
);

CREATE INDEX "index_professors_on_academic_title_country_id" ON "professors" ("academic_title_country_id");

CREATE INDEX "index_professors_on_academic_title_institution_id" ON "professors" ("academic_title_institution_id");

CREATE INDEX "index_professors_on_academic_title_level_id" ON "professors" ("academic_title_level_id");

CREATE INDEX "index_professors_on_city_id" ON "professors" ("city_id");

CREATE INDEX "index_professors_on_email" ON "professors" ("email");

CREATE INDEX "index_professors_on_institution_id" ON "professors" ("institution_id");

CREATE INDEX "index_professors_on_user_id" ON "professors" ("user_id");

CREATE TABLE IF NOT EXISTS "queries" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "sql" text,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "description" varchar(255)
);

CREATE TABLE IF NOT EXISTS "query_params" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "query_id" integer,
    "name" varchar(255),
    "default_value" varchar(255),
    "value_type" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_query_params_on_query_id" ON "query_params" ("query_id");

CREATE TABLE IF NOT EXISTS "report_configurations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "use_at_report" boolean,
    "use_at_transcript" boolean,
    "use_at_grades_report" boolean,
    "use_at_schedule" boolean,
    "text" text,
    "image" varchar(255),
    "signature_footer" boolean,
    "order" integer DEFAULT 2,
    "scale" decimal(10, 8),
    "x" integer,
    "y" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "research_areas" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "code" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "roles" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(50) NOT NULL,
    "description" varchar(255) NOT NULL,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "scholarship_durations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "scholarship_id" integer NOT NULL indirect,
    "enrollment_id" integer NOT NULL personal,
    "start_date" date indirect,
    "end_date" date indirect,
    "obs" text indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "cancel_date" date indirect
);

CREATE INDEX "index_scholarship_durations_on_enrollment_id" ON "scholarship_durations" ("enrollment_id");

CREATE INDEX "index_scholarship_durations_on_scholarship_id" ON "scholarship_durations" ("scholarship_id");

CREATE TABLE IF NOT EXISTS "scholarship_suspensions" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "start_date" date,
    "end_date" date,
    "active" boolean DEFAULT 1,
    "scholarship_duration_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_scholarship_suspensions_on_scholarship_duration_id" ON "scholarship_suspensions" ("scholarship_duration_id");

CREATE TABLE IF NOT EXISTS "scholarship_types" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "scholarships" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "scholarship_number" varchar(255) indirect,
    "level_id" integer indirect,
    "sponsor_id" integer indirect,
    "scholarship_type_id" integer indirect,
    "start_date" date indirect,
    "end_date" date indirect,
    "obs" text indirect,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "professor_id" integer personal
);

CREATE INDEX "index_scholarships_on_level_id" ON "scholarships" ("level_id");

CREATE INDEX "index_scholarships_on_professor_id" ON "scholarships" ("professor_id");

CREATE INDEX "index_scholarships_on_scholarship_type_id" ON "scholarships" ("scholarship_type_id");

CREATE INDEX "index_scholarships_on_sponsor_id" ON "scholarships" ("sponsor_id");

CREATE TABLE IF NOT EXISTS "sessions" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "session_id" varchar NOT NULL,
    "data" text,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL
);

CREATE UNIQUE INDEX "index_sessions_on_session_id" ON "sessions" ("session_id");

CREATE INDEX "index_sessions_on_updated_at" ON "sessions" ("updated_at");

CREATE TABLE IF NOT EXISTS "sponsors" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "states" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "code" varchar(255),
    "country_id" integer,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_states_on_country_id" ON "states" ("country_id");

CREATE TABLE IF NOT EXISTS "student_majors" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "major_id" integer NOT NULL,
    "student_id" integer NOT NULL
);

CREATE INDEX "index_student_majors_on_major_id" ON "student_majors" ("major_id");

CREATE INDEX "index_student_majors_on_student_id" ON "student_majors" ("student_id");

CREATE TABLE IF NOT EXISTS "students" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL personalDONE,
    "name" varchar(255) personalDONE,
    "cpf" varchar(255) personalDONE,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "obs" text indirect,
    "birthdate" date personalDONE,
    "sex" varchar(255) personalDONE,
    "civil_status" varchar(255) personalDONE,
    "father_name" varchar(255) personalDONE,
    "mother_name" varchar(255) personalDONE,
    "identity_number" varchar(255) personalDONE,
    "identity_issuing_body" varchar(255) personalDONE,
    "identity_expedition_date" date personalDONE,
    "employer" varchar(255) personalDONE,
    "job_position" varchar(255) personalDONE,
    "birth_state_id" integer personalDONE,
    "city_id" integer personalDONE,
    "neighborhood" varchar(255) personalDONE,
    "zip_code" varchar(255) personalDONE,
    "address" varchar(255) personalDONE,
    "telephone1" varchar(255) personalDONE,
    "telephone2" varchar(255) personalDONE,
    "email" varchar(255) personalDONE,
    "birth_city_id" integer personalDONE,
    "identity_issuing_place" varchar(255) personalDONE,
    "photo" varchar(255) personalDONE,
    "birth_country_id" integer personalDONE,
    "user_id" integer(8) persona[DONE]l
);

CREATE INDEX "index_students_on_birth_city_id" ON "students" ("birth_city_id");

CREATE INDEX "index_students_on_birth_country_id" ON "students" ("birth_country_id");

CREATE INDEX "index_students_on_state_id" ON "students" ("birth_state_id");

CREATE INDEX "index_students_on_city_id" ON "students" ("city_id");

CREATE INDEX "index_students_on_user_id" ON "students" ("user_id");

CREATE TABLE IF NOT EXISTS "thesis_defense_committee_participations" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL indirect,
    "professor_id" integer personal,
    "enrollment_id" integer personal,
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL
);

CREATE INDEX "index_thesis_defense_committee_participations_on_enrollment_id" ON "thesis_defense_committee_participations" ("enrollment_id");

CREATE INDEX "index_thesis_defense_committee_participations_on_professor_id" ON "thesis_defense_committee_participations" ("professor_id");

CREATE TABLE IF NOT EXISTS "users" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" varchar(255),
    "created_at" datetime NOT NULL,
    "updated_at" datetime NOT NULL,
    "email" varchar(255) DEFAULT '' NOT NULL,
    "encrypted_password" varchar(255) DEFAULT '' NOT NULL,
    "reset_password_token" varchar(255),
    "reset_password_sent_at" datetime,
    "remember_created_at" datetime,
    "sign_in_count" integer DEFAULT 0,
    "current_sign_in_at" datetime,
    "last_sign_in_at" datetime,
    "current_sign_in_ip" varchar(255),
    "last_sign_in_ip" varchar(255),
    "confirmation_token" varchar(255),
    "confirmed_at" datetime,
    "confirmation_sent_at" datetime,
    "failed_attempts" integer DEFAULT 0,
    "unlock_token" varchar(255),
    "locked_at" datetime,
    "role_id" integer DEFAULT 1 NOT NULL,
    "unconfirmed_email" varchar,
    "invitation_token" varchar,
    "invitation_created_at" datetime,
    "invitation_sent_at" datetime,
    "invitation_accepted_at" datetime,
    "invitation_limit" integer,
    "invited_by_type" varchar,
    "invited_by_id" integer,
    "invitations_count" integer DEFAULT 0
);

CREATE INDEX "index_users_on_email" ON "users" ("email");

CREATE UNIQUE INDEX "index_users_on_invitation_token" ON "users" ("invitation_token");

CREATE INDEX "index_users_on_invited_by_id" ON "users" ("invited_by_id");

CREATE INDEX "index_users_on_invited_by_type_and_invited_by_id" ON "users" ("invited_by_type", "invited_by_id");

CREATE INDEX "index_users_on_role_id" ON "users" ("role_id");

CREATE TABLE IF NOT EXISTS "versions" (
    "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    "item_type" varchar(255) NOT NULL,
    "item_id" integer NOT NULL,
    "event" varchar(255) NOT NULL,
    "whodunnit" varchar(255),
    "object" text(16777215),
    "created_at" datetime
);

CREATE INDEX "index_versions_on_item_type_and_item_id" ON "versions" ("item_type", "item_id");

CREATE TABLE IF NOT EXISTS "schema_migrations" ("version" varchar NOT NULL PRIMARY KEY);

CREATE TABLE IF NOT EXISTS "ar_internal_metadata" (
    "key" varchar NOT NULL PRIMARY KEY,
    "value" varchar,
    "created_at" datetime(6) NOT NULL,
    "updated_at" datetime(6) NOT NULL
);