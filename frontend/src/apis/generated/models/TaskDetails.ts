/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Label } from './Label';
import type { User } from './User';
export type TaskDetails = {
    title: string;
    content: string;
    message_id?: (string | null);
    due_date?: (string | null);
    id: string;
    group_id: string;
    created_at: string;
    updated_at: string;
    labels: Array<Label>;
    assigned_users: Array<User>;
};

