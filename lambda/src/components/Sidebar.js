function Sidebar () {
    return(
        <div className="sidebar">
            <div className="sidebar-header">
                <h3>Sidebar</h3>
            </div>
            <div className="sidebar-body">
                <ul className="list-group">
                    <li className="list-group-item">
                        <a href="#">Link 1</a>
                    </li>
                    <li className="list-group-item">
                        <a href="#">Link 2</a>
                    </li>
                    <li className="list-group-item">
                        <a href="#">Link 3</a>
                    </li>
                </ul>
            </div>
        </div>
    );
}


export default Sidebar;