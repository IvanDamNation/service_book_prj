interface DataProps {
    col: [];
}

const Column = ({col}: DataProps) => {
    return (
        <div>
            {col.map((data: string) => (
                <td>
                    {data}
                </td>
            ))}
        </div>
    );
};

export default Column;