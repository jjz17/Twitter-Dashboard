import React from 'react'

export default function Pagination({ gotoNextPage, gotoPrevPage }) {
  return (
    // If gotoPrevPage exists, then render the button
    <div>
      {gotoPrevPage && <button onClick={gotoPrevPage}>Previous</button>}
      {gotoNextPage && <button onClick={gotoNextPage}>Next</button>}
    </div>
  )
}