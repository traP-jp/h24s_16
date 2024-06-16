/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Label } from './Label';
export type GroupDetails = {
    id: string;
    name: string;
    remind_channel_id: (string | null);
    periodic_remind_at: (string | null);
    created_at: string;
    updated_at: string;
    user_ids: Array<string>;
    labels: Array<Label>;
};

