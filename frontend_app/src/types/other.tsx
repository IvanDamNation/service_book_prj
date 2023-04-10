import { IComplaint } from "./machine/complaint";
import { IMachine } from "./machine/machine";
import { IMaintenance } from "./machine/maintenance";


export type MainProps = IMachine[] | IComplaint[] | IMaintenance[];
