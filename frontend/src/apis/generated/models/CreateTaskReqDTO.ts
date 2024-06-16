/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type CreateTaskReqDTO = {
    title: string;
    content: string;
    message_id?: (string | null);
    due_date?: (string | null);
    group_id: string;
    labels: Array<string>;
    assigned_user_ids: Array<string>;
};

