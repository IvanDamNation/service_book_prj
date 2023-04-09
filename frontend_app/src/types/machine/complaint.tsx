export interface IComplaint {
    pk: number;
    date_of_complaint: string;
    operating_hours: number;
    unit_failure: string;
    failure_description: string;
    recovery_method: string;
    used_parts: string;
    date_of_repair: string;
    machine: string;
    service_comp: string;
}