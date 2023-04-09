import { FC } from "react";
import { IMachine } from "../../../types/machine/machine";
import Column from "./Column";
import List from "../List";

const Raw: FC<IMachine> = (parameters) => {
    return (
        <tr>
            <List 
                items={parameters}
                renderItem={(parameter: string | number) => <Column parameter={parameter} key={parameter.pk}/>}
            />
        </tr>
    );
};

export default Raw;