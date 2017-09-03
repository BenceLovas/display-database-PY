
MENTORS =                "SELECT mentors.first_name, mentors.last_name, schools.country FROM mentors \
                          INNER JOIN schools ON mentors.city = schools.city"

ALL_SCHOOL =             "SELECT \
                            COALESCE(mentors.first_name, 'No data') AS mentor_first_name, \
                            COALESCE(mentors.last_name, 'No data') AS mentor_last_name, \
                            schools.name, \
                            schools.country \
                          FROM mentors \
                          RIGHT JOIN schools ON mentors.city = schools.city \
                          ORDER BY mentors.id"

MENTORS_BY_COUNTRY =     "SELECT COUNT(mentors.id), schools.country FROM mentors \
                          INNER JOIN schools ON mentors.city = schools.city \
                          GROUP BY schools.country"
 
CONTACTS =               "SELECT schools.name, mentors.first_name, mentors.last_name FROM mentors \
                          INNER JOIN schools ON mentors.id = schools.contact_person \
                          ORDER BY schools.name"

APPLICANTS =             "SELECT \
                            applicants.first_name, \
                            applicants.application_code, \
                            applicants_mentors.creation_date \
                          FROM applicants \
                          INNER JOIN applicants_mentors \
                            ON applicants.id = applicants_mentors.applicant_id \
                            AND applicants_mentors.creation_date > '2016-01-01' \
                          ORDER BY applicants_mentors.creation_date"

APPLICANTS_AND_MENTORS = "SELECT \
                            applicants.first_name, \
                            applicants.application_code, \
                            COALESCE(mentors.first_name, 'No data') AS mentor_first_name, \
                            COALESCE(mentors.last_name, 'No data') AS mentor_last_name \
                          FROM applicants_mentors \
                          INNER JOIN mentors ON applicants_mentors.mentor_id = mentors.id \
                          RIGHT JOIN applicants ON applicants_mentors.applicant_id = applicants.id \
                          ORDER BY applicants.id"
 