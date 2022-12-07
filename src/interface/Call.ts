import React from "react";

export async function callTest(un:string,deux:string):Promise<string> {
    let path: string = "/api/essai"
    path += "?un=" + un + "&deux=" + deux;

    const response = await fetch(path).then(res => res.json()).then(data => {
        return data.te;
      ;});
      return response;
}