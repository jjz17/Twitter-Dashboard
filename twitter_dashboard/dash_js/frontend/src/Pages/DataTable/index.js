import {
  DollarCircleOutlined,
  ShoppingCartOutlined,
  ShoppingOutlined,
  UserOutlined,
} from "@ant-design/icons";
import { Card, Space, Statistic, Table, Typography } from "antd";
import { useEffect, useState } from "react";
import { getTweets } from "../../API";

function explodeTweetsJSON(tweets) {
  let explodedTweets = [];
  for (let i = 0; i < tweets.length; i++) {
    let userTweets = tweets[i];
    for (let j = 0; j < userTweets.tweets.length; j++) {
      let t = {
        "user": userTweets.user,
        "tweet": userTweets.tweets[j]
      };
      explodedTweets.push(t);
    }
  }
  console.log(explodedTweets)
  return explodedTweets;
}

const props = {
  bordered: true,
  loading: false,
  pagination: { position: "bottom" },
  size: "default",
  title: undefined,
  showHeader: true,
  rowSelection: {},
  scroll: { y: 500 }
};

const columns = [
  {
    title: "User",
    dataIndex: "user",
    key: "user",
    width: 150,
    sorter: (a, b) => a.user.localeCompare(b.user)
    // render: text => <a href="javascript:;">{text}</a>
  },
  {
    title: "Tweet",
    dataIndex: "tweet",
    key: "tweet",
    width: 200,
    render: tweet => tweet.text
  },
];

const pagination = { defaultPageSize: 10, showSizeChanger: true, pageSizeOptions: ['5', '10', '20'] }

function DataTable() {
  const [tweets, setTweets] = useState(0);

  useEffect(() => {
    getTweets().then((res) => {
      setTweets(explodeTweetsJSON(res));
      // setTweets(res[0].tweets[0].text);
      // setTweets(res[0].user);
    });
  }, []);

  return (
    <Space size={20} direction="vertical">
      <Typography.Title level={4}>Dashboard</Typography.Title>
      <Space direction="horizontal">
        <Table {...props} columns={columns} dataSource={tweets} pagination={pagination} />

        {/* <DashboardCard
                    icon={
                        <ShoppingCartOutlined
                            style={{
                                color: "green",
                                backgroundColor: "rgba(0,255,0,0.25)",
                                borderRadius: 20,
                                fontSize: 24,
                                padding: 8,
                            }}
                        />
                    }
                    title={"Tweets"}
                    value={tweets}
                />
                <DashboardCard
                    icon={
                        <ShoppingOutlined
                            style={{
                                color: "blue",
                                backgroundColor: "rgba(0,0,255,0.25)",
                                borderRadius: 20,
                                fontSize: 24,
                                padding: 8,
                            }}
                        />
                    }
                    title={"Inventory"}
                    value={100}
                /> */}
      </Space>
      <Space>
        {/* <RecentOrders />
          <DashboardChart /> */}
      </Space>
    </Space>
  );
}

function DashboardCard({ title, value, icon }) {
  return (
    <Card>
      <Space direction="horizontal">
        {icon}
        <Statistic title={title} value={value} />
      </Space>
    </Card>
  );
}

export default DataTable;