// import { getTweets } from "../../API";

// const data = [
//     {
//         name: "Jeff",
//         age: 30,
//     },
//     {
//         name: "John",
//         age: 35,
//     },
//     {
//         name: "Jason",
//         age: 20,
//     },
//     {
//         name: "Brandon",
//         age: 16,
//     },
//     {
//         name: "Lifen",
//         age: 51,
//     },
// ]


// const tweets = getTweets();
// console.log("PC: " + typeof(tweets))
// console.log("PageContent")
// console.log(tweets)

// // console.log(tweets);
// // console.log(tweets.length)

// function PageContent() {
//     return <div className="PageContent">
//         {data.map((d, key) => {
//             return (
//                 <div key={key}>
//                     {d.name +
//                         " , " +
//                         d.age}
//                 </div>
//             );
//         })}

//         <div>
//             {typeof(tweets)}
//             {console.log("Indicator")}
//             {/* {tweets.map((tweet, key) => {
//                 return (
//                     <div key={key}>
//                         {tweet.user +
//                             " , " +
//                             tweet.tweets}
//                     </div>
//                 );
//             })} */}
//         </div>
//     </div>
// }
// export default PageContent;



import AppRoutes from "../AppRoutes";

function PageContent() {
  return (
    <div className="PageContent">
      <AppRoutes />
    </div>
  );
}
export default PageContent;