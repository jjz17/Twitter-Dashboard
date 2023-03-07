import { BellFilled, MailOutlined } from "@ant-design/icons";
import { Badge, Image, Space, Typography } from "antd";

function AppHeader() {
    return <div className="AppHeader">
        <Image width={40} src="https://yt3.ggpht.com/ytc/AMLnZu83ghQ28n1SqADR-RbI2BGYTrqqThAtJbfv9jcq=s176-c-k-c0x00ffffff-no-rj"></Image>
        <Typography.Title>Twitter Dashboard</Typography.Title>
        <Space>
            <Badge count={10} dot>
            <MailOutlined style={{ fontsize: 24 }} />
            </Badge>
            <Badge count={20}>
            <BellFilled style={{ fontsize: 24 }} />
            </Badge>
        </Space>
    </div>
}
export default AppHeader;