export interface IMachine {
    pk: number;
    factory_number: string;
    model: number;
    engine: number;
    engine_num: string;
    transmission: number;
    transmission_num: string;
    rear_axle: number;
    rear_axle_num: string;
    front_axle: number;
    front_axle_num: string;
    supply_contract: string;
    shipment_date: string;
    consignee: string;
    shipment_address: string;
    equipment: string;
    client: number;
    service_comp: number;
}