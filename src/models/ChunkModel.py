from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne
from typing import List

class DataChunkModel(BaseDataModel):

    def __init__(self, db_client: object):
        super().__init__(db_client)
        self.colletion = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]

    async def create_chunk(self, chunk: DataChunk):
        result = await self.colletion.insert_one(chunk.dict(by_alias=True, exclude_none=True))
        chunk.id = result.inserted_id
        return chunk

    async def get_chunk(self, chunk_id: ObjectId):
        result = await self.colletion.find_one({"_id": ObjectId(chunk_id)})

        if result is None:
            return None

        return DataChunk(**result)

    async def insert_many_chunks(self, chunks: List[DataChunk], batch_size: int=100):
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i+batch_size]
            operations = [InsertOne(chunk.dict(by_alias=True, exclude_none=True)) for chunk in batch]
            await self.colletion.bulk_write(operations)

        return len(chunks)

    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        result = await self.colletion.delete_many({"chunk_project_id": project_id})

        return result.deleted_count

        
        

    