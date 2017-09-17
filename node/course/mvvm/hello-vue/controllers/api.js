const APIError = require('../rest').APIError;

const path = require('path');

const fs = require('mz/fs');

const saved_dir = path.normalize(__dirname + path.sep + '..' + path.sep + 'saved-docs');

console.log(`documents will be saved in ${saved_dir}.`);

var gid = 0;

function nextId() {
    gid ++;
    return 't' + gid;
}

var todos = [
    {
        id: nextId(),
        name: 'Learn Git',
        description: 'Learn how to use git as distributed version control'
    },
    {
        id: nextId(),
        name: 'Learn JavaScript',
        description: 'Learn JavaScript, Node.js, NPM and other libraries'
    },
    {
        id: nextId(),
        name: 'Learn Python',
        description: 'Learn Python, WSGI, asyncio and NumPy'
    },
    {
        id: nextId(),
        name: 'Learn Java',
        description: 'Learn Java, Servlet, Maven and Spring'
    }
];

/* 我们用数组在服务器端模拟一个数据库，然后实现以下4个API：
GET /api/todos：返回所有TODO列表；
POST /api/todos：创建一个新的TODO，并返回创建后的对象；
PUT /api/todos/:id：更新一个TODO，并返回更新后的对象；
DELETE /api/todos/:id：删除一个TODO。 */
module.exports = {
    'GET /api/todos': async (ctx, next) => {
        ctx.rest({
            todos: todos
        });
    },

    'POST /api/todos': async (ctx, next) => {
        var
            t = ctx.request.body,
            todo;
        if (!t.name || !t.name.trim()) {
            throw new APIError('invalid_input', 'Missing name');
        }
        if (!t.description || !t.description.trim()) {
            throw new APIError('invalid_input', 'Missing description');
        }
        todo = {
            id: nextId(),
            name: t.name.trim(),
            description: t.description.trim()
        };
        todos.push(todo);
        ctx.rest(todo);
    },

    'PUT /api/todos/:id': async (ctx, next) => {
        var
            t = ctx.request.body,
            index = -1,
            i, todo;
        if (!t.name || !t.name.trim()) {
            throw new APIError('invalid_input', 'Missing name');
        }
        if (!t.description || !t.description.trim()) {
            throw new APIError('invalid_input', 'Missing description');
        }
        for (i=0; i<todos.length; i++) {
            if (todos[i].id === ctx.params.id) {
                index = i;
                break;
            }
        }
        if (index === -1) {
            throw new APIError('notfound', 'Todo not found by id: ' + ctx.params.id);
        }
        todo = todos[index];
        todo.name = t.name.trim();
        todo.description = t.description.trim();
        ctx.rest(todo);
    },

    'DELETE /api/todos/:id': async (ctx, next) => {
        var i, index = -1;
        for (i=0; i<todos.length; i++) {
            if (todos[i].id === ctx.params.id) {
                index = i;
                break;
            }
        }
        if (index === -1) {
            throw new APIError('notfound', 'Todo not found by id: ' + ctx.params.id);
        }
        ctx.rest(todos.splice(index, 1)[0]);
    },


    
    'GET /api/sheets/:id': async (ctx, next) => {
        var s, fp = path.join(saved_dir, '.' + ctx.params.id);
        console.log(`load from file ${fp}...`);
        s = await fs.readFile(fp, 'utf8');
        ctx.rest(JSON.parse(s));
    },
    'PUT /api/sheets/:id': async (ctx, next) => {
        var
            fp = path.join(saved_dir, '.' + ctx.params.id),
            title = ctx.request.body.title,
            rows = ctx.request.body.rows,
            data;
        if (!title) {
            throw new APIError('invalid_data', 'invalid title');
        }
        if (!Array.isArray(rows)){
            throw new APIError('invalid_data', 'invalid rows');
        }
        data = {
            title: title,
            rows: rows
        };
        await fs.writeFile(fp, JSON.stringify({
            title: title,
            rows: rows
        }), 'utf8');
        console.log(`wrote to file ${fp}.`);
        ctx.rest({
            id: ctx.params.id
        });
    }

}
