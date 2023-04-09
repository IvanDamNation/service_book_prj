export interface IMaintenance {
    pk: number;
    type: string;
    date: string;
    operating_hours: number;
    work_order: string;
    work_order_date: string;
    maintain_corp: string;
    machine: string;
    service_comp: string; 
}