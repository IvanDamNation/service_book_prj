import React, { FC } from "react";
import { IMachine } from "../../types/machine/machine";
import { IComplaint } from "../../types/machine/complaint";
import { MainProps } from "../../types/other";
// import Raw from "./table_components/Raw";


interface TableInfoProps {
    mainProps: MainProps;
    colNames: string[];
    width?: string | number;
    height?: string | number;
}


const TableInfo: FC<TableInfoProps> = ({mainProps, colNames, width='auto', height='auto'}) => {

    return (
        <div className="tableContainer">
            <table className="searchInfoTable" cellSpacing={0} style={{ width:width, height:height }}>
                <thead>
                    <tr>
                        {colNames.map((headerItem, index) => (
                            <th key={index}>
                                {headerItem.toUpperCase()}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {Object.values(mainProps).map((obj, index) => (
                        <tr key={index}>
                            {Object.values(obj).map((value: any, index2) => (
                                <td key={index2}>
                                    {value}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default TableInfo;