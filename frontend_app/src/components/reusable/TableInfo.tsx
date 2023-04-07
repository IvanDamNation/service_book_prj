import React from "react";


const TableInfo = () => {
    return (
        <div className="tableContainer">
            <table className="searchInfoTable">
                <thead>
                    <tr>
                        <th>One</th>
                        <th>Two</th>
                        <th>Three</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td data-label="One">Four</td>
                        <td data-label="Two">Five</td>
                        <td data-label="Three">Six</td>
                    </tr>
                    <tr>
                        <td data-label="One">Seven</td>
                        <td data-label="Two">Eight</td>
                        <td data-label="Three">Nine</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}

export default TableInfo;