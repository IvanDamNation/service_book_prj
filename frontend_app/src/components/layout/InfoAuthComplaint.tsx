import { FC, useEffect, useState } from "react";
import { IComplaint } from "../../types/machine/complaint";
import NavAuth from "../reusable/NavAuth";
import axios from "axios";
import TableInfo from "../reusable/TableInfo";


const InfoAuthComplaint:FC = () => {
    const [complaints, setComplaints] = useState<IComplaint[]>([]);

    useEffect(() => {
        fetchInfo()
    }, []);

    async function fetchInfo () {
        try {
            const response = await axios.get<IComplaint[]>(
                "http://127.0.0.1:8000/service_center/complaint/"
            );
            setComplaints(response.data);
        } catch (e) {
            alert(e)
        }
    }

    const colNames = [
        "#", "Дата отказа", "Наработка, м/час", "Узел отказа", 
        "Описание отказа", "Способ восстановления", 
        "Используемые запасные части", "Дата восстановления", 
        "Mашина", "Cервисная компания"
    ]

    return (
        <div className="contentAuthTechnical">
            <p className="mainInfo">Основная панель</p>
            <div className="headerTechnical">
                <h3 className="headerTechnicalInfo">Машина 1</h3>
                <h4 className="headerTechnicalInfo">Заводской номер</h4>
            </div>
            <div className="searchInfo">
                <div className="searchInfoHeadContainer"></div>
                <h2 className="searchInfoHead">
                    Информация о проведении работ по вашим рекламациям
                </h2>
                <NavAuth />
                <TableInfo mainProps={complaints} colNames={colNames} />
            </div>
        </div>
    );
}

export default InfoAuthComplaint;