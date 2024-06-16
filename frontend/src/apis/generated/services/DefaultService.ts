/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateTaskReqDTO } from '../models/CreateTaskReqDTO';
import type { Group } from '../models/Group';
import type { GroupDetails } from '../models/GroupDetails';
import type { Label } from '../models/Label';
import type { LabelCreate } from '../models/LabelCreate';
import type { LabelUpdate } from '../models/LabelUpdate';
import type { TaskDetails } from '../models/TaskDetails';
import type { User } from '../models/User';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class DefaultService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * Get User
     * @returns User Successful Response
     * @throws ApiError
     */
    public getUserUsersMeGet(): CancelablePromise<User> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/users/me',
        });
    }
    /**
     * Get User Groups
     * @returns Group Successful Response
     * @throws ApiError
     */
    public getUserGroupsUsersGroupsGet(): CancelablePromise<Array<Group>> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/users/groups',
        });
    }
    /**
     * Get Group
     * @param groupId
     * @returns GroupDetails Successful Response
     * @throws ApiError
     */
    public getGroupGroupsGroupIdGet(
        groupId: string,
    ): CancelablePromise<GroupDetails> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/groups/{group_id}',
            path: {
                'group_id': groupId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Group Tasks
     * @param groupId
     * @returns TaskDetails Successful Response
     * @throws ApiError
     */
    public getGroupTasksGroupsGroupIdTasksGet(
        groupId: string,
    ): CancelablePromise<Array<TaskDetails>> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/groups/{group_id}/tasks',
            path: {
                'group_id': groupId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Task
     * @param requestBody
     * @returns TaskDetails Successful Response
     * @throws ApiError
     */
    public createTaskTasksPost(
        requestBody: CreateTaskReqDTO,
    ): CancelablePromise<TaskDetails> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/tasks',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Task
     * @param taskId
     * @returns any Successful Response
     * @throws ApiError
     */
    public deleteTaskTasksTaskIdDelete(
        taskId: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'DELETE',
            url: '/tasks/{task_id}',
            path: {
                'task_id': taskId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Patch Task Title
     * @param taskId
     * @param title
     * @returns any Successful Response
     * @throws ApiError
     */
    public patchTaskTitleTasksTaskIdTitlePatch(
        taskId: string,
        title: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/tasks/{task_id}/title',
            path: {
                'task_id': taskId,
            },
            query: {
                'title': title,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Patch Task Content
     * @param taskId
     * @param content
     * @returns any Successful Response
     * @throws ApiError
     */
    public patchTaskContentTasksTaskIdContentPatch(
        taskId: string,
        content: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/tasks/{task_id}/content',
            path: {
                'task_id': taskId,
            },
            query: {
                'content': content,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Patch Task Due Date
     * @param taskId
     * @param dueDate
     * @returns any Successful Response
     * @throws ApiError
     */
    public patchTaskDueDateTasksTaskIdDueDatePatch(
        taskId: string,
        dueDate: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/tasks/{task_id}/due_date',
            path: {
                'task_id': taskId,
            },
            query: {
                'due_date': dueDate,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Put Task Assignee
     * @param taskId
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public putTaskAssigneeTasksTaskIdAssigneesPatch(
        taskId: string,
        requestBody: Array<string>,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/tasks/{task_id}/assignees',
            path: {
                'task_id': taskId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Put Task Assignee
     * @param taskId
     * @param requestBody
     * @returns any Successful Response
     * @throws ApiError
     */
    public putTaskAssigneeTasksTaskIdLabelsPatch(
        taskId: string,
        requestBody: Array<string>,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/tasks/{task_id}/labels',
            path: {
                'task_id': taskId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Create Label
     * @param requestBody
     * @returns Label Successful Response
     * @throws ApiError
     */
    public createLabelLabelsPost(
        requestBody: LabelCreate,
    ): CancelablePromise<Label> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/labels',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Edit Label
     * @param labelId
     * @param requestBody
     * @returns Label Successful Response
     * @throws ApiError
     */
    public editLabelLabelsLabelIdPatch(
        labelId: string,
        requestBody: LabelUpdate,
    ): CancelablePromise<Label> {
        return this.httpRequest.request({
            method: 'PATCH',
            url: '/labels/{label_id}',
            path: {
                'label_id': labelId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Label
     * @param labelId
     * @returns any Successful Response
     * @throws ApiError
     */
    public deleteLabelLabelsLabelIdDelete(
        labelId: string,
    ): CancelablePromise<any> {
        return this.httpRequest.request({
            method: 'DELETE',
            url: '/labels/{label_id}',
            path: {
                'label_id': labelId,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
