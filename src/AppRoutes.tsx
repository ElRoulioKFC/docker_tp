import React from "react"
import { Route, Routes } from "react-router-dom"
import { NotFoundPage } from "./page"
import { HomePage } from "./home"

export function AppRoutes() {

    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="*" element={<NotFoundPage />} />
        </Routes>
    )
    }
