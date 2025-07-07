if _G.SenderLoaded then
    return
end

_G.SenderLoaded = true
local HttpService = game:GetService('HttpService')

local function requestAsync(options)
    return request(options)
end

function parsingType(type)
    if type == 'Enum.MessageType.MessageError' then
        return 'MessageError'
    elseif type == 'Enum.MessageType.MessageWarning' then
        return 'MessageWarning'
    elseif type == 'Enum.MessageType.MessageInfo' then
        return 'MessageInfo'
    elseif type == 'Enum.MessageType.MessageOutput' then
        return 'MessageOutput'
    else
        return 'MessageOutput'
    end
end

local function sendLogToServer(logMessage, messageType)
    local url = 'http://127.0.0.1:7243/console'

    local body = HttpService:JSONEncode({
        type = parsingType(messageType) or 'Info',
        message = logMessage or 'Info'
    })

    requestAsync({
        Url = url,
        Method = 'POST',
        Headers = {
            ['Content-Type'] = 'application/json'
        },
        Body = body
    })
end

local LogService = game:GetService('LogService')

LogService.MessageOut:Connect(function(message, messageType)
    sendLogToServer(message, tostring(messageType))
end)

print('[Roblox-Console] Console sender ready!')