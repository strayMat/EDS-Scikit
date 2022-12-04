default_tables_to_save = [
    "person",
    "visit_occurrence",
    "visit_detail",
    "condition_occurrence",
    "procedure_occurrence",
    "care_site",
    "concept",
]
"""
The default tables loaded when instanciating a [HiveData][eds_scikit.io.hive.HiveData]
or a [PostgresData][eds_scikit.io.postgres.PostgresData]
"""

tables_to_load = {
    "person": [
        # "key",
        "person_id",
        # "person_source_value",
        "location_id",
        # "provider_id",
        # "care_site_id",
        "year_of_birth",
        "month_of_birth",
        "day_of_birth",
        "birth_datetime",
        "death_datetime",
        # "race_concept_id",
        # "race_source_value",
        # "race_source_concept_id",
        # "ethnicity_concept_id",
        # "ethnicity_source_value",
        # "ethnicity_source_concept_id",
        # "gender_concept_id",
        "gender_source_value",
        "gender_source_concept_id",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "visit_occurrence": [
        # "key",
        "visit_occurrence_id",
        "person_id",
        "visit_occurrence_source_value",
        "preceding_visit_occurrence_id",
        # "provider_id",
        "care_site_id",
        # "visit_start_date",
        "visit_start_datetime",
        # "visit_end_date",
        "visit_end_datetime",
        # "visit_concept_id",
        "visit_source_value",
        "visit_source_concept_id",
        # "visit_type_concept_id",
        "visit_type_source_value",
        "visit_type_source_concept_id",
        # "admitted_from_concept_id",
        "admitted_from_source_value",
        "admitted_from_source_concept_id",
        # "discharge_to_concept_id",
        "discharge_to_source_value",
        "discharge_to_source_concept_id",
        # "row_status_concept_id",
        "row_status_source_value",
        # "row_status_source_concept_id",
        # "stay_concept_id",
        "stay_source_value",
        "stay_source_concept_id",
        "cdm_source",
    ],
    "care_site": [
        # "key",
        "care_site_id",
        "care_site_source_value",
        # "location_id",
        "care_site_name",
        "care_site_short_name",
        # "place_of_service_concept_id",
        "place_of_service_source_value",
        # "place_of_service_source_concept_id",
        # "care_site_type_concept_id",
        "care_site_type_source_value",
        # "care_site_type_source_concept_id",
        "valid_start_date",
        "valid_end_date",
        # "cdm_source",
    ],
    "visit_detail": [
        # "key",
        "visit_detail_id",
        "visit_occurrence_id",
        "person_id",
        "preceding_visit_detail_id",
        "visit_detail_parent_id",
        # "provider_id",
        "care_site_id",
        "visit_detail_start_date",
        "visit_detail_start_datetime",
        "visit_detail_end_date",
        "visit_detail_end_datetime",
        # "visit_detail_concept_id",
        "visit_detail_source_value",
        "visit_detail_source_concept_id",
        # "visit_detail_type_concept_id",
        "visit_detail_type_source_value",
        "visit_detail_type_source_concept_id",
        # "admitted_from_concept_id",
        "admitted_from_source_value",
        "admitted_from_source_concept_id",
        # "discharge_to_concept_id",
        "discharge_to_source_value",
        "discharge_to_source_concept_id",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "condition_occurrence": [
        # "key",
        "condition_occurrence_id",
        "person_id",
        "visit_occurrence_id",
        "visit_detail_id",
        # "provider_id",
        # "condition_start_date",
        "condition_start_datetime",
        # "condition_end_date",
        # "condition_end_datetime",
        # "condition_concept_id",
        "condition_source_value",
        "condition_source_concept_id",
        # "condition_type_concept_id",
        # "condition_type_source_value",
        # "condition_type_source_concept_id",
        # "condition_status_concept_id",
        "condition_status_source_value",
        "condition_status_source_concept_id",
        # "stop_reason",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "procedure_occurrence": [
        # "key",
        "procedure_occurrence_id",
        "person_id",
        "visit_occurrence_id",
        "visit_detail_id",
        # "provider_id",
        # "procedure_date",
        "procedure_datetime",
        # "procedure_concept_id",
        "procedure_source_value",
        "procedure_source_concept_id",
        # "procedure_type_concept_id",
        # "procedure_type_source_value",
        # "procedure_type_source_concept_id",
        # "modifier_concept_id",
        # "modifier_source_value",
        # "quantity",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    # "note": [],
    # "location": [],
    # location_history
    # measurement
    # drug_exposure
    # note_nlp
    # observation
    "concept": [
        "concept_id",
        "concept_name",
        "domain_id",
        "vocabulary_id",
        "concept_class_id",
        "standard_concept",
        "concept_code",
        "valid_start_date",
        "valid_end_date",
        "invalid_reason",
        # "hash",
    ],
    # concept_relationship
    # concept_synonym
    # fact_relationship
    # vocabulary
}
"""
The default columns loaded when instanciating a [HiveData][eds_scikit.io.hive.HiveData]
or a [PostgresData][eds_scikit.io.postgres.PostgresData]
"""

standard_terminologies = ["LOINC", "AnaBio"]
standard_concept_regex = {
    "LOINC": "[0-9]{2,5}[-][0-9]",
    "AnaBio": "[A-Z][0-9]{4}",
}

# make sure we know how to load the tables we want to save
assert all(table in tables_to_load.keys() for table in default_tables_to_save)


"""
Partial mapping from i2b2 to OMOP in order to support the functions of eds-scikit.
The idea is not to have a full mapping but to be able to the package on i2b2 extractions.
"""

map_columns_i2b2_to_omop = {
    "person": {
        "patient_num": "person_id",
        "birth_date": "birth_datetime",
        "death_date": "death_datetime",
        "sex_cd": "gender_source_value",
    },
    "condition_occurrence": {
        "encounter_num": "visit_occurrence_id",
        "patient_num": "person_id",
        "concept_cd": "condition_source_value",
        "provider_id": "provider_id",
        "start_date": "condition_start_datetime",
        "instance_num": "condition_occurrence_id",
        "tval_char": "condition_status_source_value",
        "sourcesystem_cd": "condition_type_source_value",
        "location_cd": "visit_detail_id",
    },
    "concept": None,
}

map_tables_i2b2_to_omop = {
    "i2b2_ontology": "concept",
    "i2b2_observation_cim10": "condition_occurrence",
    "i2b2_patient": "person",
}

i2b2_tables_to_load = dict()
for (
    i2b2_table_name_,
    omop_table_name_,
) in map_tables_i2b2_to_omop.items():
    column_mapping = map_columns_i2b2_to_omop[omop_table_name_]
    if column_mapping is not None:
        i2b2_tables_to_load[i2b2_table_name_] = list(column_mapping.keys())
    else:
        i2b2_tables_to_load[i2b2_table_name_] = None



def map_i2b2_to_scikiteds_omop(
    hive_data, map_table: dict[str, str], map_cols: dict[str, dict[str, str]]
):
    """Run the mapping between i2b2 and scikit-eds OMOP.
    TODO: Could be a static method of the hive_data class (because it modifies the class attributes inplace).

    Parameters
    ----------
    hive_data : _type_
        _description_
    map_table : Dict[str, str]
        Link between i2b2 table names and scikit-eds OMOP table names: {"i2b2_table_name": "omop_table_name"}
    map_cols : Dict[str, str]
        Link between i2b2 column names and scikit-eds OMOP column names: {"omop_table_name": {"i2b2_col_name": "omop_col_name"}}
    """
    # renaming tables
    for i2b2_table_name, omop_table_name in map_table.items():
        hive_data.rename_table(i2b2_table_name, omop_table_name)
        # renaming columns
        map_cols_i2b2_to_omop = map_cols[omop_table_name]
        if map_cols_i2b2_to_omop is not None:
            hive_data.__getattr__(i2b2_table_name).rename(
                columns=map_cols_i2b2_to_omop, inplace=True
            )
