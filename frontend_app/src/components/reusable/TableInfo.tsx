import { FC, useState } from "react";
import { MainProps } from "../../types/other";


interface TableInfoProps {
    mainProps: MainProps;
    colNames: string[];
    width?: string | number;
    height?: string | number;
}


const TableInfo: FC<TableInfoProps> = ({mainProps, colNames, width='auto', height='auto'}) => {

    {/*
    const [sortedList, setSortedList] = useState(mainProps);
    const [sortColumn, setSortColumn] = useState();
    const [sortAcscending, setSortAcscending] = useState(true);

    const sortByColumn = (colNameRaw: string) =>{
        let tempSortedList = [...mainProps];
        let newSortDirection = !sortAcscending;

        if (colNameRaw !== sortColumn) {
            newSortDirection = true;
            setSortColumn(colNameRaw);
        }

        if (newSortDirection) {
            tempSortedList.sort((a, b) => {
                const x= a[colNameRaw];
                const y = b[colNameRaw];
                if (x < y) {
                    return -1;
                }
                if (x > y) {
                    return 1;
                }
                return 0;
            })
        } else {
            tempSortedList.sort((a, b) => {
                const x= a[colNameRaw];
                const y = b[colNameRaw];
                if (x < y) {
                    return 1;
                }
                if (x > y) {
                    return -1;
                }
                return 0;
            })
        }

        setSortAcscending(newSortDirection);
        setSortedList(tempSortedList);
    };

    try {
        let firstObj = sortedList[0];
        let colNameRaw = Object.keys(firstObj);
        console.log(colNameRaw);
    } catch(e) {

    }
*/}

    return (
        <div className="tableContainer">
            <table className="searchInfoTable" cellSpacing={0} style={{ width:width, height:height }}>
                <thead>
                    <tr>
                        {colNames.map((headerItem, index) => (
                            <th key={index} /* onClick={(colNameRaw) => sortByColumn(colNameRaw)} */ >
                                {headerItem.toUpperCase()}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {Object.values(mainProps).map((obj, index) => (
                        <tr key={index}>
                            {/* {console.log(Object.keys(obj))} */}
                            {Object.values(obj).map((value: any, index2) => (
                                <td key={index2}>
                                    {value.toLocaleString()}
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